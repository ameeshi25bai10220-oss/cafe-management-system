from db_manager import DatabaseManager
from inventory_manager import InventoryManager
from order_manager import OrderManager
from report_generator import ReportGenerator

def initialize_data(inv_manager):
    # Populates initial data (only run once)
    inv_manager.add_menu_item("Latte", 150.00)
    # ... (other data setup)

def main():
    db_manager = DatabaseManager()
    inv_manager = InventoryManager(db_manager)
    order_manager = OrderManager(db_manager, inv_manager)
    report_generator = ReportGenerator(db_manager)
    
    # 1. SETUP
    initialize_data(inv_manager)
    
    # 2. DEMO ORDER WORKFLOW
    order_manager.place_order("Latte", 2)
    order_manager.finalize_order()
    
    # 3. DEMO REPORTING
    report_generator.generate_sales_summary()
    inv_manager.check_low_stock()
    
    db_manager.close()

if __name__ == "__main__":
    main()
