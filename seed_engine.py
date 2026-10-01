import sqlite3
import os

def initialize_mock_database():
    print("====== INITIALIZING LOGISTICAL PERSISTENCE LAYER ======\n")
    db_path = "database.db"
    
    # Establish dynamic connection string to embedded database
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    # Create the relational schema tracking unique constraints
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inventory_registry (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sku_code TEXT UNIQUE NOT NULL,
        item_name TEXT NOT NULL,
        initial_stock INTEGER NOT NULL CHECK (initial_stock >= 0)
    )
    """)
    
    # Inject a clean seed row block matching your TC-IMS-VAL-001 payload
    try:
        cursor.execute("""
        INSERT OR IGNORE INTO inventory_registry (sku_code, item_name, initial_stock)
        VALUES ('SAM-MIL-998A', 'Tactical Logistical Housing Unit', 150)
        """)
        connection.commit()
        print("  SUCCESS: Relational SQLite schema initialized successfully.")
        print("  SUCCESS: Primary stock tracking indices created.")
        print(f" DATA STATUS: Database file generated securely at: {os.path.abspath(db_path)}")
    except sqlite3.Error as e:
        print(f" DATABASE CRITICAL ERROR: Initialization halted: {e}")
    finally:
        connection.close()

    print("\n====== PERSISTENCE SEED MATRIX OPERATIONAL SUITE READY ======")

if __name__ == "__main__":
    initialize_mock_database()
