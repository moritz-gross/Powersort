#!/usr/bin/env python3
import sys
import pandas as pd
import matplotlib.pyplot as plt

def process_csv(filename):
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(filename)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        sys.exit(1)

    try:
        # Convert the average time columns to floats if they aren't already
        df['Timsort_Avg'] = df['Timsort_Avg'].astype(float)
        df['Powersort_Avg'] = df['Powersort_Avg'].astype(float)
    except Exception as e:
        print(f"Error converting time columns to float: {e}")
        sys.exit(1)

    # Calculate the ratio for each test entry
    df['ratio'] = df['Powersort_Avg'] / df['Timsort_Avg']
    return df['ratio']

def main():
    if len(sys.argv) < 2:
        print("Usage: python evaluate_csv.py <csv_file>")
        sys.exit(1)

    csv_filename = sys.argv[1]
    ratios = process_csv(csv_filename)

    if ratios.empty:
        print("No valid rows found in the CSV file.")
        sys.exit(1)

    # Plot the histogram of ratios
    plt.figure()
    plt.hist(ratios, bins='auto', edgecolor='black')
    plt.xlabel("Change from Timsort to Powersort (ratio)")
    plt.ylabel("Frequency")
    plt.title("Histogram of Sorting Time Ratios")
    plt.show()

if __name__ == '__main__':
    main()