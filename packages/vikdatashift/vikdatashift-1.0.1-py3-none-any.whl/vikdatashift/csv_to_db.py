import os
import sys
import psycopg2
import cx_Oracle
import csv
import time
import io
import json

CONFIG_FILE = 'db_config.json'

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

def read_csv_in_chunks(csv_file_path, chunk_size=100000):
    with open(csv_file_path, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)  # Read the header
        chunk = []
        for row in reader:
            chunk.append(row)
            if len(chunk) == chunk_size:
                yield header, chunk
                chunk = []
        if chunk:  # Don't forget the last chunk if it's smaller than chunk_size
            yield header, chunk

def load_csv_to_ora(cursor, csv_file_path, table_name, truncate=False):
    if truncate:
        cursor.execute(f"TRUNCATE TABLE {table_name}")

    total_rows = 0
    total_start_time = time.time()
    chunk_count = 0

    for header, chunk in read_csv_in_chunks(csv_file_path):
        chunk_start_time = time.time()
        chunk_count += 1

        if total_rows == 0:  # First chunk, we need to prepare the INSERT statement
            columns = ', '.join(header)
            placeholders = ', '.join([':' + str(i+1) for i in range(len(header))])
            insert_stmt = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

        cursor.prepare(insert_stmt)
        cursor.executemany(None, chunk)

        total_rows += len(chunk)
        chunk_end_time = time.time()
        chunk_duration = chunk_end_time - chunk_start_time

        print(f"Chunk {chunk_count}: Inserted {len(chunk)} rows into {table_name} in {chunk_duration:.2f} seconds")
        print(f"Total rows inserted so far: {total_rows}")

    total_end_time = time.time()
    total_duration = total_end_time - total_start_time
    print(f"\nTotal insertion time: {total_duration:.2f} seconds")
    print(f"Total rows inserted: {total_rows}")

def load_csv_to_pg(cursor, csv_file_path, table_name, truncate=False):
    if truncate:
        cursor.execute(f"TRUNCATE TABLE {table_name}")

    total_rows = 0
    total_start_time = time.time()
    chunk_count = 0

    try:
        for header, chunk in read_csv_in_chunks(csv_file_path):
            chunk_start_time = time.time()
            chunk_count += 1

            if total_rows == 0:  # First chunk, we need to create the COPY command
                columns = ', '.join(f'"{col}"' for col in header)
                copy_command = f"COPY {table_name} ({columns}) FROM STDIN WITH CSV"

            # Convert chunk to CSV string
            output = io.StringIO()
            writer = csv.writer(output)
            writer.writerows(chunk)
            output.seek(0)

            cursor.copy_expert(copy_command, output)

            total_rows += len(chunk)
            chunk_end_time = time.time()
            chunk_duration = chunk_end_time - chunk_start_time

            print(f"Chunk {chunk_count}: Inserted {len(chunk)} rows into {table_name} in {chunk_duration:.2f} seconds")
            print(f"Total rows inserted so far: {total_rows}")

    except psycopg2.Error as e:
        print(f"Database error: {e}")
        print(f"Error occurred at row: {total_rows + 1}")
        raise
    except Exception as e:
        print(f"Unexpected error: {e}")
        print(f"Error occurred at row: {total_rows + 1}")
        raise

    total_end_time = time.time()
    total_duration = total_end_time - total_start_time
    print(f"\nTotal insertion time: {total_duration:.2f} seconds")
    print(f"Total rows inserted: {total_rows}")

def create_table_from_csv(cursor, csv_file_path, table_name, db_type):
    with open(csv_file_path, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)

    columns = [f'"{col}" VARCHAR2(2000)' for col in header]
    if db_type=='postgres':
        columns = [f'"{col}" VARCHAR(2000)' for col in header]

    create_stmt = f"CREATE TABLE {table_name} (\n    " + ",\n    ".join(columns) + "\n)"

    print("Create Table Statement:")
    print(create_stmt)

    cursor.execute(create_stmt)
    print(f"Table {table_name} created successfully.")

def csv_to_db(db_type):
    conn = get_db_connection(db_type)
    cur = conn.cursor()

    try:
        while True:
            # Ask for CSV file name
            csv_file_name = input("Enter the name of the CSV file or ENTER to finish: ").strip()

            if csv_file_name.lower() == '':
                break

            # Ask for action
            while True:
                action = input("Enter action ('t' for truncate, 'c' for create table, or press Enter to skip): ").strip().lower()
                if action in ['t', 'c', '']:
                    break
                print("Invalid input. Please enter 't', 'c', or press Enter.")

            csv_dir = os.getcwd()
            table_name = csv_file_name  # Use the same name for the table

            csv_file_path = os.path.join(csv_dir, csv_file_name + '.csv')

            if not os.path.exists(csv_file_path):
                print(f"Error: CSV file not found: {csv_file_path}")
                continue

            print(f"Processing file: {csv_file_path}")
            print(f"Target table: {table_name}")

            if action == 'c':
                create_table_from_csv(cur, csv_file_path, table_name, db_type)
            elif action == 't':
                print("Truncate before insertion: Yes")
            else:
                print("Truncate before insertion: No")

            if db_type == 'postgres':
                load_csv_to_pg(cur, csv_file_path, table_name, truncate=(action == 't'))
            else:
                load_csv_to_ora(cur, csv_file_path, table_name, truncate=(action == 't'))

            conn.commit()
            print(f"Finished processing {csv_file_name}")
            print("---")

    except cx_Oracle.DatabaseError as e:
        conn.rollback()
        error, = e.args
        print(f"Oracle Error: {error.code} - {error.message}")
    except psycopg2.Error as e:
        conn.rollback()
        print(f"PostgreSQL Error: {e}")
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()

# csv_to_db("oracle")
# csv_to_db("postgres")
