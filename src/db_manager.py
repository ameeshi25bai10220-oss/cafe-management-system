import sqlite3
import os
import pandas as pd

class DatabaseManager:
    def __init__(self, db_name='cafe.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # Creates MENU, INVENTORY, and TRANSACTIONS tables
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS MENU (
                menu_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL UNIQUE,
                price REAL NOT NULL
            )
        ''')
        # ... (SQL for INVENTORY and TRANSACTIONS tables)
        self.conn.commit()

    def execute_query(self, query, params=()):
        # Executes INSERT, UPDATE, DELETE queries
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            return self.cursor.rowcount
        except sqlite3.Error as e:
            # Basic error handling
            return None

    def fetch_data(self, query, params=()):
        # Executes SELECT queries
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
    
    # ... (other helper functions like fetch_data_to_df)
