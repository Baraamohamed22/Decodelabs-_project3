# SQL Data Analysis Report

## Project

DecodeLabs Data Analytics Project 3: SQL Data Analysis.

## Goal

Use SQL queries to extract insights from the ecommerce order dataset.

## Dataset and Database

| Item | Value |
| --- | --- |
| Source dataset | `data/raw_dataset.xlsx` |
| SQL database | `outputs/orders.db` |
| SQL table | `orders` |
| Rows loaded | 1200 |
| Columns loaded | 14 |

## SQL Requirements Covered

- `SELECT` queries
- `WHERE` filtering
- `ORDER BY` sorting
- `GROUP BY` grouping
- `HAVING` grouped filtering
- Aggregations: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`

## Dataset Summary Query Result

| TotalOrders | UniqueCustomers | TotalUnitsSold | TotalRevenue | AverageOrderValue | MinimumOrderValue | MaximumOrderValue |
| --- | --- | --- | --- | --- | --- | --- |
| 1200.0 | 1189.0 | 3535.0 | 1264761.96 | 1053.97 | 11.39 | 3456.4 |

## Product Performance

| Product | OrderCount | UnitsSold | TotalRevenue | AverageOrderValue |
| --- | --- | --- | --- | --- |
| Chair | 178 | 562 | 195620.11 | 1098.99 |
| Printer | 181 | 542 | 195612.61 | 1080.73 |
| Laptop | 173 | 535 | 192126.56 | 1110.56 |
| Tablet | 179 | 497 | 186568.95 | 1042.28 |
| Monitor | 163 | 480 | 175651.41 | 1077.62 |
| Desk | 170 | 508 | 167459.93 | 985.06 |
| Phone | 156 | 411 | 151722.39 | 972.58 |

## Revenue by Order Status

| OrderStatus | OrderCount | TotalRevenue | AverageOrderValue |
| --- | --- | --- | --- |
| Cancelled | 250 | 276396.21 | 1105.58 |
| Returned | 247 | 243277.7 | 984.93 |
| Pending | 237 | 256328.15 | 1081.55 |
| Shipped | 235 | 246159.58 | 1047.49 |
| Delivered | 231 | 242600.32 | 1050.22 |

## Payment Method Analysis

| PaymentMethod | OrderCount | TotalRevenue | AverageOrderValue |
| --- | --- | --- | --- |
| Online | 258 | 262442.94 | 1017.22 |
| Cash | 246 | 259786.29 | 1056.04 |
| Credit Card | 234 | 263847.63 | 1127.55 |
| Debit Card | 232 | 232361.18 | 1001.56 |
| Gift Card | 230 | 246323.92 | 1070.97 |

## Monthly Revenue Trend

| YearMonth | OrderCount | UnitsSold | TotalRevenue | AverageOrderValue |
| --- | --- | --- | --- | --- |
| 2023-01 | 47 | 146 | 56685.75 | 1206.08 |
| 2023-02 | 37 | 102 | 40117.66 | 1084.26 |
| 2023-03 | 43 | 126 | 48609.37 | 1130.45 |
| 2023-04 | 31 | 84 | 27751.71 | 895.22 |
| 2023-05 | 49 | 148 | 63836.84 | 1302.79 |
| 2023-06 | 45 | 146 | 49500.19 | 1100.0 |
| 2023-07 | 44 | 119 | 42820.66 | 973.2 |
| 2023-08 | 51 | 174 | 54352.14 | 1065.73 |
| 2023-09 | 29 | 86 | 29526.67 | 1018.16 |
| 2023-10 | 47 | 150 | 52607.85 | 1119.32 |
| 2023-11 | 41 | 114 | 43079.67 | 1050.72 |
| 2023-12 | 46 | 129 | 43754.73 | 951.19 |

## Key SQL Insights

1. Total orders loaded into SQLite: 1,200.
2. Total revenue: $1,264,761.96.
3. Average order value: $1,053.97.
4. Top product by revenue: `Chair`.
5. Most common payment method: `Online`.
6. Highest revenue month: `2024-06`.
7. High-value orders with `TotalPrice >= 3000`: 34.
8. The SQL file includes all required query types for Project 3.

## Output Files

- `sql/analysis_queries.sql`
- `outputs/orders.db`
- `outputs/sql_analysis_report.md`
- `outputs/sql_summary.json`
- `outputs/query_results/preview_orders.csv`
- `outputs/query_results/high_value_orders.csv`
- `outputs/query_results/top_10_orders.csv`
- `outputs/query_results/product_performance.csv`
- `outputs/query_results/revenue_by_order_status.csv`
- `outputs/query_results/delivered_orders_by_product.csv`
- `outputs/query_results/payment_method_analysis.csv`
- `outputs/query_results/monthly_revenue_trend.csv`
- `outputs/query_results/products_over_170_orders.csv`
- `outputs/query_results/dataset_summary.csv`
