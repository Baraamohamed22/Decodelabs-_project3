# DecodeLabs Data Analytics Project 3

## SQL Data Analysis

This project uses SQL queries to extract business insights from an ecommerce order dataset. The dataset is loaded into a SQLite database, then analyzed with `SELECT`, `WHERE`, `ORDER BY`, `GROUP BY`, and aggregation queries.

## Project Requirements

- Write `SELECT` queries.
- Use `WHERE`, `ORDER BY`, and `GROUP BY`.
- Perform basic aggregations:
  - `COUNT`
  - `SUM`
  - `AVG`

## Dataset

The raw dataset is stored at:

`data/raw_dataset.xlsx`

The SQLite database generated from the dataset is:

`outputs/orders.db`

The SQL table name is:

`orders`

## Tools Used

- Python
- Pandas
- SQLite
- Excel

## SQL Analysis Performed

The project includes SQL queries for:

1. Previewing orders with `SELECT`.
2. Filtering high-value orders with `WHERE`.
3. Sorting top orders with `ORDER BY`.
4. Grouping product performance with `GROUP BY`.
5. Aggregating revenue by order status.
6. Filtering delivered orders.
7. Analyzing payment methods.
8. Finding monthly revenue trends.
9. Using `HAVING` to filter grouped product results.
10. Producing a full dataset summary with `COUNT`, `SUM`, `AVG`, `MIN`, and `MAX`.

## How to Run

Install the required Python packages:

```bash
pip install pandas openpyxl
```

Run the SQL analysis:

```bash
python sql_analysis.py
```

## Output Files

Generated files are saved in the `outputs` folder:

- `orders.db`
- `sql_analysis_report.md`
- `sql_summary.json`
- `query_results/*.csv`

The main SQL file is:

`sql/analysis_queries.sql`

## Main Deliverable

The main report for submission is:

`outputs/sql_analysis_report.md`
