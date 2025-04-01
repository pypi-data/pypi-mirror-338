import numpy as np
from xgboost import XGBRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
import xgboost as xgb

# Generate a synthetic regression dataset
X, y = make_regression(n_samples=1000, n_features=10, n_informative=8, noise=0.1, random_state=42)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and fit an XGBoost regressor model
model = XGBRegressor(n_estimators=50, learning_rate=0.1, random_state=42)
model.fit(X_train, y_train)

# Get the booster object
booster = model.get_booster()

# Convert the test data into DMatrix
dtest = xgb.DMatrix(X_test)

# Predict using all trees up to the 21st tree
pred_up_to_21 = booster.predict(dtest, iteration_range=(0, 21))

# Predict using all trees up to the 22nd tree
pred_up_to_22 = booster.predict(dtest, iteration_range=(0, 22))

# Predict using only the 21st tree
pred_only_21 = booster.predict(dtest, iteration_range=(21, 22))


pred_only_25 = booster.predict(dtest, iteration_range=(24, 25))

# Sanity check: Verify if prediction for iteration_range=(21, 22) is cumulative
is_cumulative = np.allclose(pred_up_to_22, pred_up_to_21 + pred_only_21)

print(f"Prediction using trees 0 to 21:\n{pred_up_to_21[:5]}")  # Show first 5 predictions
print(f"Prediction using trees 0 to 22:\n{pred_up_to_22[:5]}")  # Show first 5 predictions
print(f"Prediction using only tree 21:\n{pred_only_21[:5]}")    # Show first 5 predictions
print(f"Is prediction for iteration_range=(21, 22) cumulative? {is_cumulative}")
print(f"Prediction using only tree 25:\n{pred_only_25[:5]}")    # Show first 5 predictions
print("y is: ", y)