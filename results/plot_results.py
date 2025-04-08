import numpy as np
import matplotlib.pyplot as plt

# List of improvement percentages (computed as above)
improvements = np.array([23.64, 21.81, 1.41, 34.09, 35.03, 33.34, 12.37, 7.98, 0.03, -4.29])

# Define bin edges in increments of 10%
bins = np.array([-10, 0, 10, 20, 30, 40, 50])

# Calculate histogram counts using numpy
counts, _ = np.histogram(improvements, bins=bins)

print("Histogram counts:")
for i in range(len(bins)-1):
    print(f"Improvement from {bins[i]}% to {bins[i+1]}%: {counts[i]} cases")

# Plot the histogram
plt.hist(improvements, bins=bins, edgecolor='black')
plt.xlabel('Improvement Percentage (%)')
plt.ylabel('Number of Cases')
plt.title('Histogram of Improvement Percentages')
plt.xticks(bins)
plt.show()