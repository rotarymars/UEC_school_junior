import matplotlib.pyplot as plt
import pandas as pd
import os

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

# Create a list of dataframes and their labels
dataframes = [
    (df_1, "Sensor 1"),
    (df_2, "Sensor 2"),
    (df_3, "Sensor 3"),
    (df_4, "Sensor 4")
]

# Create subplots for each measurement type
# plt.figure(figsize=(15, 10))

# Plot each dataframe
print("Plotting data...")
for df, label in dataframes:
    # Assuming the first column is time and the rest are measurements
    time_col = df.columns[0]
    measurement_cols = df.columns[1:]
    
    for col in measurement_cols:
        fig, ax = plt.subplots()
        # plt.subplot(len(measurement_cols), 1, list(measurement_cols).index(col) + 1)
        ax.plot(df[time_col], df[col], label=f"{label} - {col}")
        ax.set_xlabel('Time')
        ax.set_ylabel(col)
        ax.legend()
        ax.grid(True)
        # plt.show()
        plt.savefig(f"bin/{label}_{col}.png")
