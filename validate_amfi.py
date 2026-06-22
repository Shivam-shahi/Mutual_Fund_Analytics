import pandas as pd

# Load fund master
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

print("=" * 50)
print("AMFI CODE VALIDATION REPORT")
print("=" * 50)

# Get unique codes from both files
master_codes = set(fund_master["amfi_code"].unique())
nav_codes = set(nav_history["amfi_code"].unique())

# Check which codes match
matched = master_codes.intersection(nav_codes)
missing = master_codes - nav_codes

print(f"\nTotal codes in fund_master: {len(master_codes)}")
print(f"Total codes in nav_history: {len(nav_codes)}")
print(f"Matched codes: {len(matched)}")
print(f"Missing codes: {len(missing)}")

if missing:
    print(f"\n⚠️ Missing codes: {missing}")
else:
    print("\n✅ All AMFI codes validated!")

print("=" * 50)