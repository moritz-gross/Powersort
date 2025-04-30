import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    timsort_path = 'results/2025-04-09--test3.csv'
    df = pd.read_csv(timsort_path)
    print(df.head())
    print(df["Timsort_Avg"].sum())
