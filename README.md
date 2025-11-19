# ☕ Cafe Management System (CMS)

## Overview

The Cafe Management System (CMS) is a Command Line Interface (CLI) application built with Python to digitize and automate core operations of a small cafe. It replaces error-prone, paper-based processes for orders, inventory, and sales tracking, improving efficiency and data reliability.

## Key Features

* **Order Processing:** Staff can quickly input orders, calculate totals, and finalize transactions.
* **Inventory Control:** Real-time stock tracking for ingredients/items (e.g., paper cups, coffee beans).
* **Low Stock Alerts:** Automatically flags items when their quantity falls below a predefined threshold.
* **Sales Analytics:** Generates reports on total revenue and the top-selling items.
* **Data Persistence:** All menu, inventory, and transaction data are stored reliably in a **SQLite database**.

## Technologies Used

* **Language:** Python 3.x (OOP)
* **Database:** SQLite 3
* **Libraries:** pandas, sqlite3, json, datetime

## Steps to Install & Run

1.  **Prerequisite:** Ensure Python 3.x is installed on your system.
2.  **Install Dependencies:** Open your terminal and install the required library:
    bash
    pip install pandas
  
3.  **Execute the System:** Navigate to the project directory and run the main entry point:
    bash
    python src/main.py
    

## Instructions for Testing

The main.py script automatically runs a demonstration workflow:
1.  Initializes the cafe.db database and populates sample menu/stock data.
2.  Simulates a customer order (e.g., 2 Lattes, 1 Croissant).
3.  Logs the transaction and decrements the Paper Cup stock count.
4.  Displays the updated inventory, low-stock alerts, and the final Sales Summary Report.
