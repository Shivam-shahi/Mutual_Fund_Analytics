import requests
import pandas as pd
import os
from datetime import datetime

os.makedirs("../data/raw", exist_ok=True)

schemes = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

def fetch_nav():
    print(f"🔄 Fetching NAV at {datetime.now()}")
    for name, code in schemes.items():
        url = f"https://api.mfapi.in/mf/{code}"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame(data["data"])
        df.to_csv(f"../data/raw/{name}.csv", index=False)
        print(f"✅ {name} saved - {len(df)} rows")
    print("🎉 ETL Pipeline complete!")

if __name__ == "__main__":
    fetch_nav()