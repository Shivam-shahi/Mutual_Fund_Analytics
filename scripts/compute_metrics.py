import pandas as pd
import numpy as np
import sqlite3

conn = sqlite3.connect("../bluestock_mf.db")
nav = pd.read_sql("SELECT * FROM nav_history", conn)
conn.close()

nav['date'] = pd.to_datetime(nav['date'])
nav['nav'] = pd.to_numeric(nav['nav'], errors='coerce')

metrics = []
for code in nav['amfi_code'].unique():
    fund_nav = nav[nav['amfi_code'] == code].sort_values('date')
    if len(fund_nav) < 30:
        continue
    returns = fund_nav['nav'].pct_change().dropna()
    sharpe = (returns.mean() / returns.std()) * np.sqrt(252)
    var_95 = np.percentile(returns, 5)
    metrics.append({
        'amfi_code': code,
        'sharpe_ratio': round(sharpe, 4),
        'VaR_95': round(var_95, 4)
    })

metrics_df = pd.DataFrame(metrics)
print(metrics_df.head(10))
metrics_df.to_csv("../reports/metrics_report.csv", index=False)
print("✅ Metrics computed and saved!")