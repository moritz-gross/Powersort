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
        # Ensure required columns exist
        required_columns = ['Timsort_Avg', 'Powersort_Avg', 'ArraySize']
        if not all(col in df.columns for col in required_columns):
            missing = [col for col in required_columns if col not in df.columns]
            print(f"Error: Missing required columns in CSV: {', '.join(missing)}")
            sys.exit(1)

        df['Timsort_Avg'] = pd.to_numeric(df['Timsort_Avg'], errors='coerce')
        df['Powersort_Avg'] = pd.to_numeric(df['Powersort_Avg'], errors='coerce')
        df['ArraySize'] = pd.to_numeric(df['ArraySize'], errors='coerce')

        # Drop rows where conversion failed or times are zero/negative (to avoid division errors)
        df.dropna(subset=['Timsort_Avg', 'Powersort_Avg', 'ArraySize'], inplace=True)
        df = df[df['Timsort_Avg'] > 0] # Ensure Timsort_Avg is positive for division

    except Exception as e:
        print(f"Error processing columns: {e}")
        sys.exit(1)

    if df.empty:
        print("No valid numeric data found in required columns after cleaning.")
        sys.exit(1)

    df['ratio'] = df['Powersort_Avg'] / df['Timsort_Avg']
    return df[['ArraySize', 'ratio']]

def main():
    if len(sys.argv) < 2:
        print("Usage: python evaluate_csv.py <csv_file>")
        sys.exit(1)

    csv_filename = sys.argv[1]
    data = process_csv(csv_filename)

    # --- Plotting ---

    # Create a figure with two subplots (one below the other)
    fig, axs = plt.subplots(2, 1, figsize=(8, 10)) # Adjust figsize as needed

    # Plot 1: Histogram of ratios
    axs[0].hist(data['ratio'], bins='auto', edgecolor='black')
    axs[0].set_xlabel("Change from Timsort to Powersort (ratio = Powersort_Avg / Timsort_Avg)")
    axs[0].set_ylabel("Frequency")
    axs[0].set_title("Histogram of Sorting Time Ratios")
    axs[0].grid(True, axis='y', linestyle='--', alpha=0.7)
    average_ratio = data['ratio'].mean() # Calculate the mean of the 'ratio' column
    axs[0].axvline(average_ratio, color='red', linestyle='dashed', linewidth=2,
                   label=f'Average Ratio: {average_ratio:.3f}') # Add label for the legend
    axs[0].legend()

    # Plot 2: Scatter plot of Ratio vs ArraySize
    # Using a logarithmic scale for ArraySize if sizes vary widely
    axs[1].scatter(data['ratio'], data['ArraySize'], alpha=0.6)
    axs[1].set_xlabel("Change from Timsort to Powersort (ratio = Powersort_Avg / Timsort_Avg)")
    axs[1].set_ylabel("Input Array Size")
    axs[1].set_title("Performance Ratio vs. Input Array Size")
    axs[1].set_yscale('log') # Use log scale for x-axis if sizes span orders of magnitude
    axs[1].grid(True, linestyle='--', alpha=0.7)

    plt.tight_layout() # Adjust layout to prevent titles/labels overlapping
    plt.show() # Display the plots

if __name__ == '__main__':
    main()