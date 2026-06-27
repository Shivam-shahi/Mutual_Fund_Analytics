# Data Dictionary - Mutual Fund Analytics

## 01_fund_master.csv
| Column | Data Type | Description |
|--------|-----------|-------------|
| amfi_code | Integer | Unique AMFI scheme code |
| fund_house | String | Name of the fund house |
| scheme_name | String | Full name of the scheme |
| category | String | Equity/Debt/Hybrid |
| plan | String | Regular or Direct |
| expense_ratio_pct | Float | Annual expense ratio % |
| risk_grade | String | Risk level of the fund |

## 02_nav_history.csv
| Column | Data Type | Description |
|--------|-----------|-------------|
| amfi_code | Integer | AMFI scheme code |
| date | Date | NAV date |
| nav | Float | Net Asset Value |

## 08_investor_transactions.csv
| Column | Data Type | Description |
|--------|-----------|-------------|
| transaction_type | String | SIP/Lumpsum/Redemption |
| amount | Float | Transaction amount |
| date | Date | Transaction date |

## 07_scheme_performance.csv
| Column | Data Type | Description |
|--------|-----------|-------------|
| amfi_code | Integer | AMFI scheme code |
| return_1yr_pct | Float | 1 year return % |
| return_3yr_pct | Float | 3 year return % |
| expense_ratio_pct | Float | Expense ratio % |
| risk_grade | String | Risk grade 