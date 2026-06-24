import pandas as pd
import os

os.makedirs("data/processed", exist_ok=True)

# Clean nav_history.csv
print("Cleaning nav_history.csv...")
nav = pd.read_csv("data/raw/02_nav_history.csv")
print("nav_history columns:", nav.columns.tolist())
nav['date'] = pd.to_datetime(nav['date'])
nav = nav.sort_values(['amfi_code', 'date'])
nav = nav.dropna()
nav = nav[nav['nav'] > 0]
nav = nav.drop_duplicates()
nav.to_csv("data/processed/nav_history_clean.csv", index=False)
print(f"✅ nav_history cleaned - Shape: {nav.shape}")

# Clean investor_transactions.csv
print("\nCleaning investor_transactions.csv...")
trans = pd.read_csv("data/raw/08_investor_transactions.csv")
print("investor_transactions columns:", trans.columns.tolist())
trans = trans.drop_duplicates()
trans.to_csv("data/processed/investor_transactions_clean.csv", index=False)
print(f"✅ investor_transactions cleaned - Shape: {trans.shape}")

# Clean scheme_performance.csv
print("\nCleaning scheme_performance.csv...")
perf = pd.read_csv("data/raw/07_scheme_performance.csv")
print("scheme_performance columns:", perf.columns.tolist())
perf = perf.dropna()
perf.to_csv("data/processed/scheme_performance_clean.csv", index=False)
print(f"✅ scheme_performance cleaned - Shape: {perf.shape}")

    print("\n🎉 All files cleaned