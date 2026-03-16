import sqlite3
import pandas as pd

# Load the cleaned CSV
df = pd.read_csv('cleaned_sales.csv')

# Create in-memory SQLite database
conn = sqlite3.connect(':memory:')

# Load DataFrame into SQLite
df.to_sql('cleaned_sales', conn, index=False, if_exists='replace')

# SQL query to find highest earning customer(s)
query = """
WITH n1 AS (
    SELECT customer, SUM(amount) AS total_amount
    FROM cleaned_sales
    GROUP BY customer
), 
n2 AS (
    SELECT customer, total_amount,
           DENSE_RANK() OVER (ORDER BY total_amount DESC) AS rn
    FROM n1
)
SELECT *
FROM n2
WHERE rn = 1;
"""

# Execute query and show results
result = pd.read_sql_query(query, conn)
print(result)

# Close the connection
conn.close()
