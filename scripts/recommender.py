import pandas as pd
import sqlite3

def recommend_funds(risk_appetite):
    conn = sqlite3.connect("../bluestock_mf.db")
    performance = pd.read_sql("SELECT * FROM scheme_performance", conn)
    fund_master = pd.read_sql("SELECT * FROM fund_master", conn)
    conn.close()
    
    top3 = performance.nlargest(3, 'sharpe_ratio')[
        ['scheme_name', 'sharpe_ratio', 'return_1yr_pct', 'risk_grade']
    ]
    
    print(f"\n🎯 Top 3 funds for {risk_appetite} risk:")
    print(top3)
    return top3

if __name__ == "__main__":
    recommend_funds("Low")
    recommend_funds("Moderate") 
    recommend_funds("High")
    print("✅ Recommender done!")