from sklearn.datasets import fetch_california_housing
import numpy as np
from stats_confidence_intervals.core import mean_confidence_interval, plot_confidence_interval
import matplotlib.pyplot as plt

# Load California housing dataset
housing = fetch_california_housing()
data = housing.data
target = housing.target
feature_names = housing.feature_names

# Create subplots for features
fig, axes = plt.subplots(4, 2, figsize=(15, 12))
axes = axes.ravel()

for i, (feature, ax) in enumerate(zip(feature_names, axes)):
    # Calculate 95% confidence interval
    ci = mean_confidence_interval(data[:, i])
    
    # Print results
    print(f"\n{feature}:")
    print(f"Mean: {ci.estimate:.2f}")
    print(f"95% CI: ({ci.lower_bound:.2f}, {ci.upper_bound:.2f})")
    
    # Set the current axis
    plt.sca(ax)
    
    # Plot confidence interval
    plot_confidence_interval(ci, label=feature)
    plt.title(f"{feature} Distribution")
    
    # Adjust axis limits for better visualization
    margin = (ci.upper_bound - ci.lower_bound) * 0.2
    plt.xlim(ci.lower_bound - margin, ci.upper_bound + margin)
    plt.ylim(0.5, 1.5)

plt.tight_layout()
plt.show()

# Create figure for house prices
plt.figure(figsize=(10, 3))
price_ci = mean_confidence_interval(target)
print("\nHouse Prices (100k USD):")
print(f"Mean: ${price_ci.estimate:.2f}00,000")
print(f"95% CI: (${price_ci.lower_bound:.2f}00,000, ${price_ci.upper_bound:.2f}00,000)")

plot_confidence_interval(price_ci, label="House Price (100k USD)", create_figure=True)

# Compare prices by house age
plt.figure(figsize=(12, 4))

# Split data by median age
median_age = np.median(data[:, 6])
old_houses = target[data[:, 6] > median_age]
new_houses = target[data[:, 6] <= median_age]

# Calculate confidence intervals
old_ci = mean_confidence_interval(old_houses)
new_ci = mean_confidence_interval(new_houses)

print("\nPrice Comparison by House Age:")
print("Older Houses:")
print(f"Mean: ${old_ci.estimate:.2f}00,000")
print(f"95% CI: (${old_ci.lower_bound:.2f}00,000, ${old_ci.upper_bound:.2f}00,000)")

print("\nNewer Houses:")
print(f"Mean: ${new_ci.estimate:.2f}00,000")
print(f"95% CI: (${new_ci.lower_bound:.2f}00,000, ${new_ci.upper_bound:.2f}00,000)")

# Plot both intervals on the same figure
plot_confidence_interval(old_ci, y_offset=1.2)
plot_confidence_interval(new_ci, y_offset=0.8)

plt.title("House Prices by Age")
plt.xlabel("Price (100k USD)")
plt.yticks([0.8, 1.2], ["Newer Houses", "Older Houses"])
plt.grid(True, alpha=0.3)

# Adjust x-axis limits for better visualization
all_prices = np.concatenate([old_houses, new_houses])
min_price, max_price = np.min(all_prices), np.max(all_prices)
margin = (max_price - min_price) * 0.1
plt.xlim(min_price - margin, max_price + margin)

plt.show() 