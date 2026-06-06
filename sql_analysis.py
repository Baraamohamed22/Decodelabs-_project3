from pathlib import Path
import json
import re
import sqlite3

import pandas as pd


ROOT_DIR = Path(__file__).resolve().parent
RAW_DATA_PATH = ROOT_DIR / "data" / "raw_dataset.xlsx"
DATABASE_PATH = ROOT_DIR / "outputs" / "orders.db"
QUERY_FILE_PATH = ROOT_DIR / "sql" / "analysis_queries.sql"
RESULTS_DIR = ROOT_DIR / "outputs" / "query_results"
REPORT_PATH = ROOT_DIR / "outputs" / "sql_analysis_report.md"
SUMMARY_PATH = ROOT_DIR / "outputs" / "sql_summary.json"


QUERY_NAMES = [
    "preview_orders",
    "high_value_orders",
    "top_10_orders",
    "product_performance",
    "revenue_by_order_status",
    "delivered_orders_by_product",
    "payment_method_analysis",
    "monthly_revenue_trend",
    "products_over_170_orders",
    "dataset_summary",
]


def load_dataset() -> pd.DataFrame:
    df = pd.read_excel(RAW_DATA_PATH, sheet_name="Sheet1")
    df.columns = [column.strip() for column in df.columns]

    text_columns = df.select_dtypes(include=["object", "string"]).columns
    for column in text_columns:
        df[column] = (
            df[column]
            .astype("string")
            .str.strip()
            .str.replace(r"\s+", " ", regex=True)
        )

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce").dt.strftime("%Y-%m-%d")
    for column in ["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    df["CouponCode"] = df["CouponCode"].fillna("NO_COUPON")
    return df


def create_database(df: pd.DataFrame) -> None:
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
    if DATABASE_PATH.exists():
        DATABASE_PATH.unlink()

    with sqlite3.connect(DATABASE_PATH) as conn:
        df.to_sql("orders", conn, index=False, if_exists="replace")
        conn.execute("CREATE INDEX idx_orders_order_id ON orders(OrderID);")
        conn.execute("CREATE INDEX idx_orders_date ON orders(Date);")
        conn.execute("CREATE INDEX idx_orders_product ON orders(Product);")
        conn.execute("CREATE INDEX idx_orders_status ON orders(OrderStatus);")


def parse_queries(sql_text: str) -> list[str]:
    without_comments = re.sub(r"--.*", "", sql_text)
    queries = [query.strip() for query in without_comments.split(";") if query.strip()]
    return queries


def run_queries() -> dict[str, pd.DataFrame]:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    queries = parse_queries(QUERY_FILE_PATH.read_text(encoding="utf-8"))

    if len(queries) != len(QUERY_NAMES):
        raise ValueError(f"Expected {len(QUERY_NAMES)} queries but found {len(queries)}.")

    results = {}
    with sqlite3.connect(DATABASE_PATH) as conn:
        for name, query in zip(QUERY_NAMES, queries):
            result = pd.read_sql_query(query, conn)
            results[name] = result
            result.to_csv(RESULTS_DIR / f"{name}.csv", index=False)
    return results


def dataframe_to_markdown(df: pd.DataFrame, max_rows: int = 10) -> str:
    display_df = df.head(max_rows).copy()
    headers = [str(column) for column in display_df.columns]
    table = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for _, row in display_df.iterrows():
        values = [str(row[column]) for column in display_df.columns]
        table.append("| " + " | ".join(values) + " |")
    return "\n".join(table)


def write_report(results: dict[str, pd.DataFrame], summary: dict) -> None:
    product_table = dataframe_to_markdown(results["product_performance"])
    status_table = dataframe_to_markdown(results["revenue_by_order_status"])
    payment_table = dataframe_to_markdown(results["payment_method_analysis"])
    monthly_table = dataframe_to_markdown(results["monthly_revenue_trend"], max_rows=12)
    dataset_summary_table = dataframe_to_markdown(results["dataset_summary"])

    report = f"""# SQL Data Analysis Report

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
| Rows loaded | {summary["rows_loaded"]} |
| Columns loaded | {summary["columns_loaded"]} |

## SQL Requirements Covered

- `SELECT` queries
- `WHERE` filtering
- `ORDER BY` sorting
- `GROUP BY` grouping
- `HAVING` grouped filtering
- Aggregations: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`

## Dataset Summary Query Result

{dataset_summary_table}

## Product Performance

{product_table}

## Revenue by Order Status

{status_table}

## Payment Method Analysis

{payment_table}

## Monthly Revenue Trend

{monthly_table}

## Key SQL Insights

1. Total orders loaded into SQLite: {summary["total_orders"]:,}.
2. Total revenue: ${summary["total_revenue"]:,.2f}.
3. Average order value: ${summary["average_order_value"]:,.2f}.
4. Top product by revenue: `{summary["top_product_by_revenue"]}`.
5. Most common payment method: `{summary["top_payment_method"]}`.
6. Highest revenue month: `{summary["highest_revenue_month"]}`.
7. High-value orders with `TotalPrice >= 3000`: {summary["high_value_order_count"]}.
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
"""
    REPORT_PATH.write_text(report, encoding="utf-8")


def build_summary(results: dict[str, pd.DataFrame], df: pd.DataFrame) -> dict:
    dataset_summary = results["dataset_summary"].iloc[0]
    product_performance = results["product_performance"].iloc[0]
    payment_method = results["payment_method_analysis"].iloc[0]
    monthly = results["monthly_revenue_trend"]
    highest_month = monthly.loc[monthly["TotalRevenue"].idxmax()]

    return {
        "rows_loaded": int(len(df)),
        "columns_loaded": int(len(df.columns)),
        "total_orders": int(dataset_summary["TotalOrders"]),
        "unique_customers": int(dataset_summary["UniqueCustomers"]),
        "total_units_sold": int(dataset_summary["TotalUnitsSold"]),
        "total_revenue": float(dataset_summary["TotalRevenue"]),
        "average_order_value": float(dataset_summary["AverageOrderValue"]),
        "top_product_by_revenue": str(product_performance["Product"]),
        "top_payment_method": str(payment_method["PaymentMethod"]),
        "highest_revenue_month": str(highest_month["YearMonth"]),
        "high_value_order_count": int(len(results["high_value_orders"])),
        "query_count": len(results),
    }


def main() -> None:
    df = load_dataset()
    create_database(df)
    results = run_queries()
    summary = build_summary(results, df)
    SUMMARY_PATH.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    write_report(results, summary)

    print("Project 3 SQL analysis complete.")
    print(f"Database: {DATABASE_PATH}")
    print(f"Report: {REPORT_PATH}")
    print(f"Query results: {RESULTS_DIR}")


if __name__ == "__main__":
    main()
