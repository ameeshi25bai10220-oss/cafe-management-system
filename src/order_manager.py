# --- Initial Data Population ---

print("--- Populating Menu ---")
inv_manager.add_menu_item("Latte", 150.00)
inv_manager.add_menu_item("Cappuccino", 180.00)
inv_manager.add_menu_item("Croissant", 80.00)
inv_manager.add_menu_item("Black Coffee", 100.00)

print("\n--- Populating Inventory Stock ---")
# Item: Name, Quantity (g/L/units), Low Stock Threshold
inv_manager.add_stock_item("Coffee Beans (g)", 5000, 1000) 
inv_manager.add_stock_item("Milk (L)", 40, 10)
inv_manager.add_stock_item("Flour (kg)", 10, 5)
inv_manager.add_stock_item("Paper Cups", 200, 50)


# --- Testing the 'Read' Functions ---

print("\n\n--- TEST 1: View Menu ---")
inv_manager.view_menu()

print("\n\n--- TEST 2: View Inventory ---")
inv_manager.view_stock()

print("\n\n--- TEST 3: Check Low Stock (Initial) ---")
inv_manager.check_low_stock()

# --- Simulating a Low Stock Condition ---

print("\n\n--- TEST 4: Low Stock Alert ---")
# Update Milk stock (ID 2) from 40L down to 5L (below the 10L threshold)
query = "UPDATE INVENTORY SET stock_qty = ? WHERE inv_id = ?"
db_manager.execute_query(query, (5, 2))
print("Simulating: Milk stock reduced to 5L.")

# Re-check the stock
inv_manager.check_low_stock()
