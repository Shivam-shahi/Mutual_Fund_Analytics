import pandas as pd
import os

# List all CSV files in data/raw
csv_folder = "data/raw"
files = os.listdir(csv_folder)

print("=" * 50)
print("DATA INGESTION REPORT")
print("=" * 50)

anomalies = []

for file in files:
    if file.endswith(".csv"):
        path = os.path.join(csv_folder, file)
        df = pd.read_csv(path)
        
        print(f"\n📁 File: {file}")
        print(f"   Shape: {df.shape}")
        print(f"   Dtypes:\n{df.dtypes}")
        print(f"   Head:\n{df.head()}")
        
        # Check anomalies
        nulls = df.isnull().sum().sum()
        if nulls > 0:
            anomalies.append(f"{file} has {nulls} missing values")

print("\n" + "=" * 50)
print("ANOMALIES FOUND:")
if anomalies:
    for a in anomalies:
        print(f"  ⚠️ {a}")
else:
    print("  ✅ No anomalies found!")
print("=" * 50)