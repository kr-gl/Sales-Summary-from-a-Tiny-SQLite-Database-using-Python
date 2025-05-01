# Sales-Summary-from-a-Tiny-SQLite-Database-using-Python

## Basic Sales Summary using SQLite and Python
This project demonstrates how to create, query, and visualize a basic sales dataset using **SQLite** for data storage and **Python** for data analysis and visualization. 

### Objective
The main objective of this project is to:
- Create a simple sales dataset using SQLite
- Run SQL queries to get total quantity sold and revenue per product
- Visualize the results using a bar chart
- Demonstrate data processing from database to visualization using Python

### Tools Used
- **Python 3**
- **SQLite** (via Python’s built-in `sqlite3` module)
- **pandas** (for data handling)
- **matplotlib** (for data visualization)

### Files
- `create_sales_data.py`: Creates the SQLite database `sales_data.db` and populates it with sample sales data.
- `sales_data.db`: Script to query and visualize sales data.
- `sales_summary.py`: Connects to the database, runs SQL queries, displays results, and plots a revenue bar chart.
- `sales_chart.png`: Output image displaying a bar chart showing revenue by product.

### Steps to Run
1. Navigate to the project folder:
   ```bash
   cd sales_summary_project
   ```
2. **Step 1: Create the SQLite database and populate it**
   ```bash
   python create_sales_data.py
   ```
3. **Step 2: Run the analysis and generate chart**
   ```bash
   python sales_summary.py
   ```
This will:
   - Print total quantity and revenue per product
   - Plot a bar chart of revenue by product
   - Save the chart as `sales_chart.png`
   - Show the chart window

### How It Works
- **create_sales_data.py**:
  - Connects to SQLite and creates a `sales` table.
  - Inserts dummy product sales data (product, quantity, price).
- **sales_summary.py**:
  - Connects to the same database.
  - Uses SQL to calculate:
    - Total quantity sold per product
    - Total revenue per product
  - Loads results into a DataFrame using pandas.
  - Prints the summary.
  - Plots revenue by product as a bar chart using matplotlib.

### Output
Printed Output:
```
Sales Summary:
  product  total_qty  revenue
0   Apple         45     54.0
1  Banana         50     25.0
2  Orange         35     28.0
```
Generated Chart:
- `sales_chart.png` (Bar chart of revenue by product)
