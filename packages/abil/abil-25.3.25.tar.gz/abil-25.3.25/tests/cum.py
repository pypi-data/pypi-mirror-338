import numpy as np
from xgboost import XGBRegressor, DMatrix
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt

# Generate synthetic data
X, y = make_regression(n_samples=1000, n_features=10, noise=0.1, random_state=42)
y = (y - y.min()) * (10000 - 100) / (y.max() - y.min()) + 100  # Scale to 100-10,000

# Train model
model = XGBRegressor(n_estimators=50, learning_rate=0.1, random_state=42)
model.fit(X, y)
booster = model.get_booster()
dtest = DMatrix(X[:5])  # Test on first 5 samples

# Your current approach: Sum individual tree predictions (i,i+1)
your_preds = np.zeros(5)
your_approach = []
for i in range(50):
    pred = booster.predict(dtest, iteration_range=(i, i+1))
    your_preds += pred * model.learning_rate  # Manual cumulative sum
    your_approach.append(your_preds.copy())

# Correct approach: Direct cumulative prediction (0,i+1)
correct_approach = []
for i in range(1, 51):
    pred = booster.predict(dtest, iteration_range=(0, i))
    correct_approach.append(pred)

# Convert to arrays for comparison
your_approach = np.array(your_approach)
correct_approach = np.array(correct_approach)

# Verify equality
print("Max absolute difference:", np.max(np.abs(your_approach - correct_approach)))
print("Are results identical?", np.allclose(your_approach, correct_approach))

# Plot progression for first sample
plt.figure(figsize=(10, 6))
plt.plot(your_approach[:, 0], label='Your Approach (sum (i,i+1))')
plt.plot(correct_approach[:, 0], '--', label='Correct (0,i+1)')
plt.xlabel("Number of Trees")
plt.ylabel("Prediction Value")
plt.title("Prediction Progression: Your Method vs Correct Method")
plt.legend()
plt.show()