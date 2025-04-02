import os
import cx_Oracle
import psycopg2
import csv
import json
import time

CONFIG_FILE = 'db_config.json'
def clean_data(data):
    """Remove NUL characters from data."""
    return [(str(item).replace('\x00', '') if isinstance(item, str) else item) for item in data]

def export_to_csv(cursor, table_name, csv_file_path):
    """Export data from a table to CSV file."""
    cursor.execute(f'SELECT * FROM {table_name}')
    data = [tuple(row) for row in cursor.fetchall()]
    columns = [desc[0] for desc in cursor.description]

    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(columns)
        for row in data:
            writer.writerow(clean_data(row))

def load_config():
    """Load configuration from file or create if not exists."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_config(config):
    """Save configuration to file."""
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=2)
def get_db_connection(db_type):
    """Get database connection based on user input or saved config."""
    config = load_config()

    if db_type not in config:
        config[db_type] = {}

    if not config[db_type]:
        print(f"Enter {db_type.capitalize()} database details:")
        if db_type == 'oracle':
            config[db_type]['user'] = input("Enter Oracle db username: ").strip()
            config[db_type]['password'] = input("Enter Oracle db password: ").strip()
            config[db_type]['host'] = input("Enter Oracle db host: ").strip()
            config[db_type]['port'] = input("Enter Oracle db port (press Enter for 1521): ").strip() or '1521'
            config[db_type]['sid'] = input("Enter Oracle db SID: ").strip()
            config[db_type]['service_name'] = input("Enter Oracle db service_name: ").strip()
        elif db_type == 'postgres':
            config[db_type]['dbname'] = input("Enter PostgreSQL db name: ").strip()
            config[db_type]['user'] = input("Enter PostgreSQL db username: ").strip()
            config[db_type]['password'] = input("Enter PostgreSQL db password: ").strip()
            config[db_type]['host'] = input("Enter PostgreSQL db host (press Enter for localhost): ").strip() or 'localhost'
            config[db_type]['port'] = input("Enter PostgreSQL db port (press Enter for 5432): ").strip() or '5432'

        save_config(config)
    if db_type == 'oracle':
        dsn = cx_Oracle.makedsn(config[db_type]['host'], config[db_type]['port'], config[db_type]['sid'])
        if config[db_type]['sid'] == "":
            dsn = cx_Oracle.makedsn(config[db_type]['host'], config[db_type]['port'], service_name=config[db_type]['service_name'])
        return cx_Oracle.connect(config[db_type]['user'], config[db_type]['password'], dsn)
    elif db_type == 'postgres':
        return psycopg2.connect(**config[db_type])
    else:
        raise ValueError("Unsupported database type")

def db_to_csv(db_type):
    """Export tables from specified database to CSV files."""
    conn = get_db_connection(db_type)
    cursor = conn.cursor()

    while True:
        table_name = input("Enter table name to export (or ENTER to finish): ")
        if table_name.lower() == '':
            break

        csv_file_path = f"{table_name}.csv"
        try:
            start_time = time.time()
            export_to_csv(cursor, table_name, csv_file_path)
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Exported {table_name} to {csv_file_path} from {db_type} in {elapsed_time:.2f} seconds.")
        except Exception as e:
            print(f"Error exporting {table_name}: {str(e)}")

    cursor.close()
    conn.close()

# if __name__ == "__main__":
#     print("Select database type:")
#     print("1. Oracle")
#     print("2. PostgreSQL")
#     choice = input("Enter your choice (1 or 2): ")

#     if choice == '1':
#         db_to_csv('oracle')
#     elif choice == '2':
#         db_to_csv('postgres')
#     else:
#         print("Invalid choice. Exiting.")