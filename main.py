import matplotlib.pyplot as plt
import pandas as pd
import os
from tqdm import tqdm

print("Reading data...")
file_1 = "data/c2a41857411e-2-2-2.csv"
file_2 = "data/cd3abcfa16f1-2-1-2.csv"
file_3 = "data/eb255017f29e-2-3-2.csv"
file_4 = "data/ed0923370eac-2-4-2.csv"
print("Done")

print("Parsing data...")
df_1 = pd.read_csv(file_1)
df_2 = pd.read_csv(file_2)
df_3 = pd.read_csv(file_3)
df_4 = pd.read_csv(file_4)
print("Done")

dataframes = [
    (df_1, "Sensor 1"),
    (df_2, "Sensor 2"),
    (df_3, "Sensor 3"),
    (df_4, "Sensor 4")
]

print("Plotting data...")
for df, label in tqdm(dataframes):
    time_col = df.columns[0]
    measurement_cols = df.columns[1:]
    
    for col in tqdm(measurement_cols):
        fig, ax = plt.subplots()
        ax.plot(df[time_col], df[col], label=f"{label} - {col}")
        ax.set_xlabel('Time')
        ax.set_ylabel(col)
        ax.legend()
        ax.grid(True)
        plt.savefig(f"bin/{label}_{col}.png")
print("Done")