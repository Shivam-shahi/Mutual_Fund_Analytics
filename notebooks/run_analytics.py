import pandas as pd
import numpy as np
import sqlite3

# Connect to your SQLite database file (adjust path if needed)
conn = sqlite3.connect("../bluestock_mf.db")

try:
    # Load data from your database
    df = pd.read_sql_query("SELECT amfi_code, date, nav FROM fact_nav ORDER BY amfi_code, date", conn)
    df['date'] = pd.to_datetime(df['date'])

    # Calculate daily returns grouped by each individual fund
    df['daily_return'] = df.groupby('amfi_code')['nav'].pct_change()

    # Drop rows without matching previous days
    df = df.dropna().reset_index(drop=True)

    print("\n--- STEP 1 COMPLETE: Daily Returns Calculated ---")
    print(df[['amfi_code', 'date', 'nav', 'daily_return']].head(10))
    
except Exception as e:
    print("Error loading data:", e)

finally:
    conn.close()