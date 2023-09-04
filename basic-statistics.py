import numpy as np
from scipy import stats

# Sample data
data = [12, 15, 18, 22, 25, 28, 31, 35, 38, 41]

# Calculate the mean (average) of the data
mean = np.mean(data)
print(f"Mean: {mean}")

# Calculate the median of the data
median = np.median(data)
print(f"Median: {median}")

# Calculate the mode of the data
mode = stats.mode(data)
print(f"Mode: {mode.mode[0]} (Occurred {mode.count[0]} times)")

# Calculate the variance of the data
variance = np.var(data)
print(f"Variance: {variance}")

# Calculate the standard deviation of the data
std_deviation = np.std(data)
print(f"Standard Deviation: {std_deviation}")

# Calculate the range of the data
data_range = np.ptp(data)
print(f"Range: {data_range}")

# Calculate the 25th and 75th percentiles (quartiles)
quartiles = np.percentile(data, [25, 75])
print(f"25th Percentile (Q1): {quartiles[0]}")
print(f"75th Percentile (Q3): {quartiles[1]}")

# Calculate the interquartile range (IQR)
iqr = quartiles[1] - quartiles[0]
print(f"IQR: {iqr}")

# Calculate the z-scores for each data point
z_scores = stats.zscore(data)
print(f"Z-Scores: {z_scores}")

# Calculate the correlation coefficient between two datasets (example)
dataset1 = [1, 2, 3, 4, 5]
dataset2 = [2, 3, 4, 5, 6]
correlation_coefficient = np.corrcoef(dataset1, dataset2)[0, 1]
print(f"Correlation Coefficient: {correlation_coefficient}")
