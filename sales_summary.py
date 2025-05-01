# File: sales_summary.py

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Connect to the SQLite database
conn = sqlite3.connect("sales_data.db")

# Step 2: Define and run the SQL query
query = """
SELECT product, 
       SUM(quantity) AS total_qty, 
       SUM(quantity * price) AS revenue 
FROM sales 
GROUP BY product
"""
df = pd.read_sql_query(query, conn)

# Step 3: Print the results
print("Sales Summary:")
print(df)

# Step 4: Plot the bar chart
df.plot(kind='bar', x='product', y='revenue', title='Revenue by Product')
plt.ylabel("Revenue")
plt.tight_layout()  # Improve layout

# Step 5: Save the chart
plt.savefig("sales_chart.png")

# Step 6: Show the plot
plt.show()

# Step 7: Close the database connection
conn.close()