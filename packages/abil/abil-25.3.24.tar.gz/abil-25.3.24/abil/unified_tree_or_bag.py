import numpy as np
import pandas as pd
import warnings
from sklearn.metrics import mean_absolute_error, balanced_accuracy_score

from sklearn.model_selection import KFold
from sklearn.preprocessing import FunctionTransformer
from sklearn.ensemble import (
    RandomForestRegressor,
    RandomForestClassifier,
    BaggingRegressor,
    BaggingClassifier,
    VotingRegressor,
    VotingClassifier,
)
from sklearn.compose import TransformedTargetRegressor
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn import base
from joblib import delayed, Parallel

from sklearn.base import is_regressor

from .zir import ZeroInflatedRegressor
from . import utils as u

def estimate_prediction_quantiles(
    model, X_predict, X_train, y_train, cv=None, chunksize=20_000, threshold=0.5
):
    """
    Train the model using cross-validation, compute predictions on X_train with summary stats,
    and predict on X_predict with summary stats.

    Parameters:
    -----------
    X_train : DataFrame
        Training feature set with MultiIndex for coordinates.

    y_train : Series
        Target values corresponding to X_train.

    X_predict : DataFrame
        Feature set to predict on, with MultiIndex for coordinates.

    m : sklearn pipeline

    cv_splits : int, default=5
        Number of cross-validation splits.

    method : str, default="rf"
        Method type for handling different model-specific behaviors:
        "rf" for RandomForestRegressor,
        "bagging" for BaggingRegressor,
        "xgb" for XGBRegressor.

    Returns:
    --------
    dict
        Dictionary containing summary statistics for both training and prediction datasets.
        Keys: "train_stats", "predict_stats".
    """
    if isinstance(model, Pipeline):
        pipeline = model
        model = pipeline.named_steps["estimator"]
    else:
        pipeline = Pipeline(
            [("preprocessor", FunctionTransformer()), ("estimator", model)]
        )
    preprocessor = pipeline.named_steps["preprocessor"]

    if X_train is not None:
        X_train = pd.DataFrame(
            preprocessor.transform(X_train),
            index = getattr(X_train, "index", np.arange(X_train.shape[0])),
            columns=X_train.columns  
        )
    if X_predict is not None:
        X_predict = pd.DataFrame(
            preprocessor.transform(X_predict),
            index = getattr(X_predict, "index", np.arange(X_train.shape[0])),
            columns=X_predict.columns  
        )
    if y_train is not None:
        y_train = pd.Series(
            y_train,
            index = getattr(y_train, "index", np.arange(y_train.shape[0]))
        )

    # X_train = preprocessor.transform(X_train)
    # X_predict = preprocessor.transform(X_predict)


    # for internal, create models for each fold to mimic the
    # effect of leaving a fold out. Do this in parallel.

    if isinstance(model, ZeroInflatedRegressor):
        classifier_stats = estimate_prediction_quantiles(
            model.classifier_,
            X_predict = X_predict,
            X_train = X_train,
            y_train = y_train > 0,
            cv=cv,
            chunksize=chunksize,
            threshold=threshold
        )
        regressor_stats = estimate_prediction_quantiles(
            model.regressor_, X_predict=X_predict, X_train=X_train, y_train=y_train, cv=cv, chunksize=chunksize, threshold=threshold
        )
        return {
            **{f"classifier_{k}": v for k, v in classifier_stats.items()},
            **{f"regressor_{k}": v for k, v in regressor_stats.items()},
        }

    if cv is not None:
        train_summary_stats = [
            _summarize_predictions(
                model,
                X_predict=X_train.iloc[test_idx],
                X_train=X_train.iloc[train_idx],
                y_train=y_train.iloc[train_idx],
                chunksize=chunksize,
                threshold=threshold
            )
            for train_idx, test_idx in cv.split(X_train, y_train)
        ]
        # concat and rearrange to match input data order
        train_summary_stats = pd.concat(
            train_summary_stats, axis=0, ignore_index=False
        ).loc[X_train.index]
    else:
        train_summary_stats = _summarize_predictions(
            model,
            X_train=X_train,
            X_predict=X_train,
            y_train=y_train,
            chunksize=chunksize,
            threshold=threshold
        )
    predict_summary_stats = _summarize_predictions(
        model, X_predict=X_predict, chunksize=chunksize, threshold=threshold
    )

    return {"train_stats": train_summary_stats, "predict_stats": predict_summary_stats}


def _summarize_predictions(model, X_predict, X_train=None, y_train=None, chunksize=2e4, threshold=0.5):
    if (X_train is not None) & (y_train is not None):
        print("model not cloned")
    elif not all([(X_train is None), (y_train is None)]):
        if not base.check_is_fitted(model):
            raise ValueError(
                "model provided is not fit, and no data is provided to fit the model on. Fit the model on the data first."
            )
        raise ValueError("Both X_train and y_train must be provided, or neither must be.")

    n_samples, n_features = X_predict.shape
    if chunksize is not None:
        n_chunks = int(np.ceil(n_samples / chunksize))
        chunks = np.array_split(X_predict, n_chunks)
        # Convert each chunk to pandas DataFrame
        chunks = [pd.DataFrame(chunk, columns=X_predict.columns) for chunk in chunks]
    else:
        chunks = [X_predict]

    stats = []
    inverse_transform = getattr(
        model, "inverse_func", FunctionTransformer().inverse_func
    )

    engine = Parallel()

    if is_regressor(model):
        proba = False
    else:
        proba = True


    # Compute predictions on X_train to estimate member performance
    if X_train is not None and y_train is not None:
        if u.is_xgboost_model(model):
            print("model is XGBoost")
            n_estimators = u.xgboost_get_n_estimators(model)
            print("n_estimators: ", n_estimators)
            if n_estimators==None:
                raise ValueError("n_estimators not inferred correctly!")

            booster = u.get_booster_from_model(model, X_train, y_train, proba)
            print(booster)
            train_pred_jobs = (
                delayed(u._predict_one_member)(i, member=booster, chunk=X_train, proba=proba, threshold=threshold)
                for i in range(n_estimators)
            )
        else:
            members, features_for_members = _flatten_metaensemble(model)
            train_pred_jobs = (
                delayed(u._predict_one_member)(
                    _,
                    member=member,
                    chunk=X_train.iloc[:, features_for_member],
                    proba=proba, 
                    threshold=threshold
                )
                for _, (features_for_member, member) in enumerate(zip(features_for_members, members))
            )
        
        train_results = engine(train_pred_jobs)

        if proba:
            print("model is a classifier")  # for debug
            losses = 1 - np.array([balanced_accuracy_score(y_train.astype(int), pred.astype(int)) for pred in train_results])

        else:
            print("model is a regressor")  # for debug
            losses = np.array([mean_absolute_error(y_train, pred) for pred in train_results])

        weights = 1 / (losses + 1e-99)  # Avoid division by zero
        weights /= weights.sum()  # Normalize weights
    else:
        weights = None  # Use equal weights if no X_train/y_train
    

    # Compute predictions on X_predict
    for chunk in chunks:
        if u.is_xgboost_model(model):
            print("model is XGBoost")
            n_estimators = u.xgboost_get_n_estimators(model)
        #    print("n_estimators: ", n_estimators)

            if n_estimators==None:
                raise ValueError("n_estimators not inferred correctly!")

            booster = u.get_booster_from_model(model, X_train, y_train, proba)
            pred_jobs = (
                delayed(u._predict_one_member)(i, member=booster, chunk=chunk, proba=proba, threshold=threshold)
                for i in range(n_estimators)
            )
        else:
            print("model not Booster")
            members, features_for_members = _flatten_metaensemble(model)
        #    print("members: ", len(members))
            pred_jobs = (
                delayed(u._predict_one_member)(
                    _,
                    member=member,
                    chunk=chunk.iloc[:, features_for_member], 
                    proba=proba, 
                    threshold=threshold
                )
                for _, (features_for_member, member) in enumerate(zip(features_for_members, members))
            )
        
        results = engine(pred_jobs)
        print("results.shape: ", np.column_stack(results).shape)
        try:
            chunk_preds = pd.DataFrame(
                inverse_transform(np.column_stack(results)),
                index=getattr(chunk, "index", None),
            )
        #    print("model uses log") 
        except:
            chunk_preds = pd.DataFrame(
                np.column_stack(results),
                index=getattr(chunk, "index", None),
            )
        #    print("model does not use log")

        if weights is not None:
            lower = chunk_preds.apply(u.weighted_quantile, q=0.025, weights=weights, axis=1)
            upper =  chunk_preds.apply(u.weighted_quantile, q=0.975, weights=weights, axis=1)
        else:
            lower = chunk_preds.quantile(q=0.025, axis=1)
            upper =  chunk_preds.quantile(q=0.975, axis=1)

        chunk_stats = pd.DataFrame(
            np.column_stack((lower, upper)), # stats we've calculated by chunk
            columns=['ci95_LL', 'ci95_UL'], # column names for the stats
            index = chunk.index # the index of the chunk, so we can align the results back to X_predict
        )
        stats.append(chunk_stats)
    
    output = pd.concat(stats, axis=0, ignore_index=False)
    return output

def _flatten_metaensemble(me):
    """
    Memoized version of the recursive meta-ensemble unpacking
    """
    estimators = [(me,None)]
    estimators_and_feature_indices = []
    while estimators:
        member, member_features = estimators.pop(0)
        if isinstance(member, ZeroInflatedRegressor):
            raise NotImplementedError("Cannot flatten a heterogeneous ensemble of classifiers and regressors")
        elif isinstance(member, Pipeline):
            estimators.append((member.named_steps['estimator'], list(np.arange(member.named_steps['estimator'].n_features_in_))))
        elif isinstance(member, TransformedTargetRegressor):
            estimators.append((member.regressor_, list(np.arange(member.regressor_.n_features_in_))))
        elif hasattr(member, "estimators_"):
            submembers_features = getattr(member, "estimators_features_", [list(np.arange(member.n_features_in_))]*len(member.estimators_))
            estimators.extend(list(zip(member.estimators_, submembers_features)))
        else:
            estimators_and_feature_indices.append((member, member_features))
    estimators, features = zip(*estimators_and_feature_indices)
    return estimators, features

# Example Usage
if __name__ == "__main__":
    # Generate sample data
    from sklearn.datasets import make_regression
    from joblib import parallel_backend  # this is user-facing
    from abil.utils import ZeroInflatedRegressor, ZeroStratifiedKFold

    X, y = make_regression(n_samples=100, n_features=10, noise=0.1)
    X_train = pd.DataFrame(X, columns=[f"feature_{i}" for i in range(X.shape[1])])
    latitudes = np.random.uniform(-90, 90, size=X_train.shape[0])
    longitudes = np.random.uniform(-180, 180, size=X_train.shape[0])
    X_train.index = pd.MultiIndex.from_tuples(
        zip(latitudes, longitudes), names=["Latitude", "Longitude"]
    )
    y_train = pd.Series(y)

    X_predict, _ = make_regression(n_samples=20, n_features=10, noise=0.1)
    X_predict = pd.DataFrame(
        X_predict, columns=[f"feature_{i}" for i in range(X_predict.shape[1])]
    )
    latitudes_predict = np.random.uniform(-90, 90, size=X_predict.shape[0])
    longitudes_predict = np.random.uniform(-180, 180, size=X_predict.shape[0])
    X_predict.index = pd.MultiIndex.from_tuples(
        zip(latitudes_predict, longitudes_predict), names=["Latitude", "Longitude"]
    )

    cv_splits = 5
    # Define cross-validation strategy
    # cv = ZeroStratifiedKFold(n_splits=cv_splits)
    cv = KFold(n_splits=cv_splits)

    # Define model and method
    model = RandomForestRegressor(n_estimators=100, max_depth=4, random_state=42).fit(
        X_train, y_train
    )

    vmodel = VotingRegressor(
        estimators=[
            (
                "rf",
                RandomForestRegressor(n_estimators=100, max_depth=4, random_state=42),
            ),
            (
                "knn",
                BaggingRegressor(
                    KNeighborsRegressor(n_neighbors=10, weights="distance"),
                    n_estimators=50,
                ).fit(X_train, y_train),
            ),
        ]
    ).fit(X_train, y_train)

    mask = (y_train > 0).values
    zirmodel = ZeroInflatedRegressor(
        BaggingClassifier(
            KNeighborsClassifier(n_neighbors=10, weights="distance"), n_estimators=50
        ),        BaggingRegressor(

            KNeighborsRegressor(n_neighbors=10, weights="distance"), n_estimators=50
        ),
    ).fit(X_train, y_train)

    v_of_zirmodels = VotingRegressor(
        estimators=[
            ("rf-then-knn", zirmodel),
            (
                "knn-then-rf",
                ZeroInflatedRegressor(
                    BaggingClassifier(
                        KNeighborsClassifier(n_neighbors=10, weights="distance"),
                        n_estimators=50,
                    ).fit(X_train, mask),
                    RandomForestRegressor(
                        n_estimators=100, max_depth=4, random_state=2245
                    ).fit(X_train.iloc[mask, :], y_train.iloc[mask]),
                ),
            ),
        ]
    ).fit(X_train, y_train)

    zir_of_vmodels = ZeroInflatedRegressor(
        classifier=VotingClassifier(
            estimators=[
                ("rfc", RandomForestClassifier(
                    n_estimators=100, max_depth=4, random_state=2245
                )),
                ("bagnnc", BaggingClassifier(
                    KNeighborsClassifier(n_neighbors=10, weights="distance"),
                    n_estimators=50,
                )),
            ]
        ),
        regressor=VotingRegressor(
            estimators=[
                ("rfr", RandomForestRegressor(n_estimators=100, max_depth=4, random_state=2245)),
                ("bagnnr", BaggingRegressor(
                    KNeighborsRegressor(n_neighbors=10, weights="distance"),
                    n_estimators=50,
                ))
            ]
        ),
    ).fit(X_train, y_train)

    # this sets the backend type and number of jobs to use in the internal
    # Parallel() call.
    with parallel_backend("loky", n_jobs=16):
        results = estimate_prediction_quantiles(
            model, X_predict=X_predict, X_train=X_train, y_train=y_train, cv=cv
        )
    with parallel_backend("loky", n_jobs=16):
        vresults = estimate_prediction_quantiles(
            vmodel, X_predict=X_predict, X_train=X_train, y_train=y_train, cv=cv
        )
    with parallel_backend("loky", n_jobs=16):
        zirresults = estimate_prediction_quantiles(
            zirmodel, X_predict=X_predict, X_train=X_train, y_train=y_train, cv=cv
        )
    with parallel_backend("loky", n_jobs=16):
        vzir_results = estimate_prediction_quantiles(
            zir_of_vmodels, X_predict=X_predict, X_train=X_train, y_train=y_train, cv=cv
        )
    print("\n=== Training Summary Stats ===\n", results["train_stats"].head())
    print("\n=== Prediction Summary Stats ===\n", results["predict_stats"].head())

    print("\n=== Training Summary Stats ===\n", vzir_results["classifier_train_stats"].head())
    print("\n=== Prediction Summary Stats ===\n", vzir_results["classifier_predict_stats"].head())
    
    print("\n=== Training Summary Stats ===\n", vzir_results["regressor_train_stats"].head())
    print("\n=== Prediction Summary Stats ===\n", vzir_results["regressor_predict_stats"].head())
