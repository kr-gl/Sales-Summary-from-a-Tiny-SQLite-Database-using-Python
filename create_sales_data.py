# File: create_sales_data.py
import sqlite3

# Connect to the database (this will create the file if it doesn't exist)
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Create a sales table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

# Insert some sample data
cursor.executemany("""
INSERT INTO sales (product, quantity, price)
VALUES (?, ?, ?)
""", [
    ("Apple", 30, 1.2),
    ("Banana", 20, 0.5),
    ("Orange", 25, 0.8),
    ("Apple", 15, 1.2),
    ("Banana", 30, 0.5),
    ("Orange", 10, 0.8)
])

conn.commit()
conn.close()