import sqlite3
import pandas as pd

conn = sqlite3.connect("bluestock_mf.db")

queries = {
    "Top 5 funds by AUM": "SELECT fund_house, SUM(aum_crore) as total_aum FROM aum_by_fund_house GROUP BY fund_house ORDER BY total_aum DESC LIMIT 5",
    "Funds with expense ratio < 1%": "SELECT scheme_name, expense_ratio_pct FROM scheme_performance WHERE expense_ratio_pct < 1 ORDER BY expense_ratio_pct",
    "Transactions by type": "SELECT transaction_type, COUNT(*) as count FROM investor_transactions GROUP BY transaction_type",
    "Top 5 funds by 1yr return": "SELECT scheme_name, return_1yr_pct FROM scheme_performance ORDER BY return_1yr_pct DESC LIMIT 5",
    "Funds by category": "SELECT category, COUNT(*) as total FROM fund_master GROUP BY category",
}

for title, query in queries.items():
    print(f"\n{'='*50}")
    print(f"📊 {title}")
    print('='*50)
    df = pd.read_sql_query(query, conn)
    print(df)

conn.close()
print("\n✅ All queries executed!")