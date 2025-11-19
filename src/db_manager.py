import sqlite3
import os
import pandas as pd
from datetime import datetime

class DatabaseManager:
    """Handles the connection and creation of the cafe database tables."""
    
    def __init__(self, db_name='cafe.db'):
        # 1. Check if the database file should be placed in a 'data' folder
        #    We will just put it in the same folder as the notebook for simplicity.
        self.db_name = db_name
        
        # 2. Connect to the database file (it creates the file if it doesn't exist)
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        
        # 3. Create the necessary tables
        self.create_tables()

    def create_tables(self):
        """Defines the structure (schema) for our database."""
        
        # Table 1: MENU (What we sell)
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS MENU (
                menu_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL UNIQUE,
                price REAL NOT NULL
            )
        ''')
                
      # Table 2: INVENTORY (Our raw ingredients/stock)
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS INVENTORY (
                inv_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL UNIQUE,
                stock_qty INTEGER NOT NULL,
                low_stock_level INTEGER NOT NULL
            )
        ''')
        
        # Table 3: TRANSACTIONS (Record of every sale)
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS TRANSACTIONS (
                trans_id INTEGER PRIMARY KEY,
                order_details TEXT NOT NULL,  -- We'll store item name and qty here
                total_amount REAL NOT NULL,
                timestamp TEXT NOT NULL
            )
        ''')
        
        self.conn.commit()
        print(f"Database '{self.db_name}' initialized successfully with three tables.")
    def execute_query(self, query, params=()):
        """A simple function to run any INSERT, UPDATE, or DELETE query."""
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            return self.cursor.rowcount
        except sqlite3.Error as e:
            # We add a basic error check (Non-functional Requirement: Reliability)
            print(f"🚨 Database Error: {e}")
            return None

    def fetch_data(self, query, params=()):
        """A simple function to retrieve data using a SELECT query."""
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
    
    def fetch_data_to_df(self, query, params=(), columns=None):
        """Helper to display table data cleanly in a Pandas DataFrame."""
        data = self.fetch_data(query, params)
        if columns is None:
            # Try to get column names from the cursor description if possible
            columns = [description[0] for description in self.cursor.description]
        return pd.DataFrame(data, columns=columns)

    def close(self):
        """Closes the connection."""
        self.conn.close()
# Initialize the Database Manager for use in other steps
db_manager = DatabaseManager()
