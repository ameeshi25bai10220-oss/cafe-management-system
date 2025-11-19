# Imports...

class InventoryManager:
    def __init__(self, db_manager):
        self.db = db_manager

    def add_menu_item(self, name: str, price: float):
        query = "INSERT INTO MENU (name, price) VALUES (?, ?)"
        return self.db.execute_query(query, (name, price))

    def update_stock_qty(self, inv_id: int, new_qty: int):
        # The crucial function used by OrderManager to decrement stock
        query = "UPDATE INVENTORY SET stock_qty = ? WHERE inv_id = ?"
        return self.db.execute_query(query, (new_qty, inv_id))

    def check_low_stock(self):
        query = "SELECT inv_id, name, stock_qty, low_stock_level FROM INVENTORY WHERE stock_qty <= low_stock_level"
        low_items = self.db.fetch_data_to_df(query, columns=["ID", "Ingredient", "Current Qty", "Low Level"])
        # ... (logic to print alert)
        return low_items
