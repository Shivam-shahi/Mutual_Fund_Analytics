"""
recommender.py
Simple Fund Recommender - Day 6 Deliverable
Capstone Project I - Mutual Fund Analytics

Input: risk appetite (Low / Moderate / High / Very High)
Output: top 3 funds by Sharpe ratio within the matching risk_grade.
"""

import pandas as pd


def load_data():
    return pd.read_csv('../data/processed/scheme_performance_clean.csv')


def recommend_funds(risk_appetite: str, data: pd.DataFrame, top_n: int = 3) -> pd.DataFrame:
    risk_appetite = risk_appetite.strip().title()
    filtered = data[data['risk_grade'].str.strip().str.title() == risk_appetite]

    if filtered.empty:
        print(f"No funds found for risk grade '{risk_appetite}'. "
              f"Available risk grades: {sorted(data['risk_grade'].dropna().unique())}")
        return pd.DataFrame()

    top_funds = filtered.sort_values('sharpe_ratio', ascending=False).head(top_n)
    return top_funds[['scheme_name', 'amfi_code', 'fund_house', 'risk_grade', 'sharpe_ratio']].reset_index(drop=True)


def main():
    data = load_data()
    print("=== Simple Fund Recommender ===")
    risk_appetite = input("Enter risk appetite (Low / Moderate / High / Very High): ").strip()

    result = recommend_funds(risk_appetite, data, top_n=3)

    if not result.empty:
        print(f"\nTop {len(result)} funds for '{risk_appetite}' risk appetite (by Sharpe ratio):\n")
        print(result.to_string(index=False))
    else:
        print("No recommendation could be generated.")


if __name__ == "__main__":
    main()