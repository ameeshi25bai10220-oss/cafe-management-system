import sqlite3
import os
import pandas as pd
from datetime import datetime
# Assuming DatabaseManager is defined in Code Cell 1

class InventoryManager:
    """
    Handles all business logic for the Menu and Ingredient Stock.
    (Functional Requirements: CRUD & Low Stock Alert)
    """
    
    def __init__(self, db_manager: sqlite3.Connection):
        self.db = db_manager

    # --- MENU MANAGEMENT ---

    def add_menu_item(self, name: str, price: float):
        """Adds a new item to the MENU table."""
        query = "INSERT INTO MENU (name, price) VALUES (?, ?)"
        return self.db.execute_query(query, (name, price))

    def view_menu(self):
        """Fetches and displays all items on the menu."""
        query = "SELECT menu_id, name, price FROM MENU ORDER BY menu_id"
        # Use the helper function to show data nicely
        df = self.db.fetch_data_to_df(query, columns=["ID", "Name", "Price (₹)"])
        print("\n--- Current Menu ---")
        return df

    # --- STOCK MANAGEMENT ---
    
    def add_stock_item(self, name: str, qty: int, low_level: int):
        """Adds a new ingredient to the INVENTORY table."""
        query = "INSERT INTO INVENTORY (name, stock_qty, low_stock_level) VALUES (?, ?, ?)"
        return self.db.execute_query(query, (name, qty, low_level))

    # THIS IS THE FUNCTION THAT WAS MISSING AND CAUSED THE ERROR
    def update_stock_qty(self, inv_id: int, new_qty: int):
        """Updates the stock quantity for an existing inventory item."""
        if new_qty < 0:
            print("Error: New quantity cannot be negative.")
            return False
            
        query = "UPDATE INVENTORY SET stock_qty = ? WHERE inv_id = ?"
        result = self.db.execute_query(query, (new_qty, inv_id))
        
        if result == 1:
            # print(f"✅ Inventory ID {inv_id} updated to {new_qty} units.") # Commented out for cleaner finalize_order output
            return True
        elif result == 0:
            print(f"❌ Error: Inventory ID {inv_id} not found.")
        return False
        
    def view_stock(self):
        """Fetches and displays all items in inventory."""
        query = "SELECT inv_id, name, stock_qty, low_stock_level FROM INVENTORY ORDER BY inv_id"
        df = self.db.fetch_data_to_df(query, columns=["ID", "Ingredient", "Qty", "Low Level"])
        print("\n--- Current Inventory Stock ---")
        return df
    def check_low_stock(self):
        """Checks and displays items that are below their low stock level."""
        query = "SELECT inv_id, name, stock_qty, low_stock_level FROM INVENTORY WHERE stock_qty <= low_stock_level"
        low_items = self.db.fetch_data_to_df(query, columns=["ID", "Ingredient", "Current Qty", "Low Level"])
        
        if low_items.empty:
            print("🟢 All stock levels are sufficient.")
        else:
            print("🚨 LOW STOCK ALERT 🚨")
            return low_items
        return low_items

    
# Initialize the Inventory Manager
inv_manager = InventoryManager(db_manager)
