-- Query 1: Top 5 funds by AUM
SELECT fund_house, SUM(aum_crore) as total_aum
FROM aum_by_fund_house
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;

-- Query 2: Average NAV per month
SELECT strftime('%Y-%m', date) as month, ROUND(AVG(nav), 2) as avg_nav
FROM nav_history
GROUP BY month
ORDER BY month;

-- Query 3: Transactions by type
SELECT transaction_type, COUNT(*) as count
FROM investor_transactions
GROUP BY transaction_type;

-- Query 4: Funds with expense ratio less than 1%
SELECT scheme_name, expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

-- Query 5: Top 5 funds by 1 year return
SELECT scheme_name, return_1yr_pct
FROM scheme_performance
ORDER BY return_1yr_pct DESC
LIMIT 5;

-- Query 6: Count funds by category
SELECT category, COUNT(*) as total_funds
FROM fund_master
GROUP BY category;

-- Query 7: SIP inflows by year
SELECT strftime('%Y', month) as year, SUM(sip_amount_crore) as total_sip
FROM monthly_sip_inflows
GROUP BY year;

-- Query 8: Top sectors by portfolio holdings
SELECT sector, COUNT(*) as holdings
FROM portfolio_holdings
GROUP BY sector
ORDER BY holdings DESC
LIMIT 5;

-- Query 9: Funds by risk grade
SELECT risk_grade, COUNT(*) as count
FROM fund_master
GROUP BY risk_grade;

-- Query 10: Average returns by category
SELECT category, ROUND(AVG(return_1yr_pct), 2) as avg_return
FROM scheme_performance
GROUP BY category
ORDER BY avg_return DESC;