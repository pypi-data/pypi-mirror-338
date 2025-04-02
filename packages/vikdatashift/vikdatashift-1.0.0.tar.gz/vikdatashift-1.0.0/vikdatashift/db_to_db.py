import os
import cx_Oracle
import psycopg2
import csv
import io
import json
import time
from psycopg2.extras import execute_values

CONFIG_FILE = 'db_config.json'
def clean_data(data):
    """Remove NUL characters from data."""
    return [(str(item).replace('\x00', '') if isinstance(item, str) else item) for item in data]

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

def create_table(cursor, table_name, columns, target_type):
    """Create a new table with the given columns."""
    column_definitions = ', '.join([f'"{col}" VARCHAR2(2000)' for col in columns])
    if target_type == 'postgres':
        column_definitions = ', '.join([f'"{col}" VARCHAR(2000)' for col in columns])

    create_query = f'CREATE TABLE {table_name} ({column_definitions})'
    cursor.execute(create_query)

def transfer_data(source_conn, target_conn, source_table, target_table, source_type, target_type):
    """Transfer data from source table to target table."""
    source_cursor = source_conn.cursor()
    target_cursor = target_conn.cursor()

    # Fetch column names
    source_cursor.execute(f'SELECT * FROM {source_table} WHERE 1=0')
    columns = [desc[0] for desc in source_cursor.description]

    # Ask user for table operation
    operation = input("Enter operation (t: truncate, c: create, or press Enter to append): ").lower()

    if operation == 't':
        target_cursor.execute(f'TRUNCATE TABLE {target_table}')
        print(f"Table {target_table} truncated.")
    elif operation == 'c':
        create_table(target_cursor, target_table, columns, target_type)
        print(f"Table {target_table} created.")

    # Fetch data from source table in chunks
    chunk_size = 100000
    source_cursor.execute(f'SELECT * FROM {source_table}')

    total_rows = 0
    total_start_time = time.time()
    while True:
        chunk_start_time = time.time()
        chunk = source_cursor.fetchmany(chunk_size)
        if not chunk:
            break

        # Clean data
        cleaned_chunk = [clean_data(row) for row in chunk]

        if target_type == 'postgres':
            # Use COPY EXPERT for PostgreSQL
            columns_str = ', '.join(f'"{col}"' for col in columns)
            copy_sql = f"COPY {target_table} ({columns_str}) FROM STDIN WITH CSV"

            csv_file = io.StringIO()
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(cleaned_chunk)
            csv_file.seek(0)

            target_cursor.copy_expert(sql=copy_sql, file=csv_file)

        elif target_type == 'oracle':
            # Use executemany for Oracle
            placeholders = ','.join([':' + str(i + 1) for i in range(len(columns))])
            insert_query = f'INSERT INTO {target_table} ({",".join(columns)}) VALUES ({placeholders})'
            target_cursor.executemany(insert_query, cleaned_chunk)

        target_conn.commit()
        total_rows += len(cleaned_chunk)

        chunk_end_time = time.time()
        chunk_duration = chunk_end_time - chunk_start_time

        print(f"Sent {len(cleaned_chunk)} rows from {source_table} ({source_type}) to {target_table} ({target_type}) in {chunk_duration:.2f} seconds")
        print(f"Total rows transferred so far: {total_rows}")

    total_end_time = time.time()
    total_duration = total_end_time - total_start_time

    print(f"Total rows transferred: {total_rows} from {source_table} ({source_type}) to {target_table} ({target_type})")
    print(f"Total transfer time: {total_duration:.2f} seconds")

def db_to_db(source_type, target_type):
    """Transfer data between Oracle and PostgreSQL databases."""
    # print("Select source database type:")
    # print("1. Oracle")
    # print("2. PostgreSQL")
    # source_choice = input("Enter your choice (1 or 2): ")

    # print("\nSelect target database type:")
    # print("1. Oracle")
    # print("2. PostgreSQL")
    # target_choice = input("Enter your choice (1 or 2): ")
    if source_type == target_type:
        print("Source and target databases must be different. Exiting.")
        return

    # source_type = 'oracle' if source_choice == '1' else 'postgres'
    # target_type = 'oracle' if target_choice == '1' else 'postgres'
    source_conn = get_db_connection(source_type)
    target_conn = get_db_connection(target_type)

    while True:
        source_table = input("Enter source table name (or ENTER to finish): ")
        if source_table.lower() == '':
            break

        target_table = input("Enter target table name: ")

        try:
            transfer_data(source_conn, target_conn, source_table, target_table, source_type, target_type)
        except Exception as e:
            print(f"Error transferring data: {str(e)}")

    source_conn.close()
    target_conn.close()

# if __name__ == "__main__":
    # db_to_db("oracle", "postgres")
#     db_to_db("postgres", "oracle")

