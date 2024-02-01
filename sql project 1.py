import mysql.connector
import csv

# Step 1: Ingest a CSV file
csv_file_path = 'Intern.csv'
database_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'project',
}

# Create a MySQL connection and cursor
conn = mysql.connector.connect(**database_config)
cursor = conn.cursor()

# Create a table name based on the CSV file name
table_name = 'people'

# Read CSV file and create the table
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    headers = next(csv_reader)  # Assuming the first row is headers
    columns = ', '.join([f'`{header}` VARCHAR(255)' for header in headers])
    create_table_query = f'CREATE TABLE IF NOT EXISTS {table_name} ({columns});'
    cursor.execute(create_table_query)

    # Ingest data from CSV
    for row in csv_reader:
        placeholders = ', '.join(['%s' for _ in range(len(row))])
        insert_query = f'INSERT INTO {table_name} VALUES ({placeholders});'
        cursor.execute(insert_query, row)

# Commit changes and close connection
conn.commit()
conn.close()

# Step 2: Create a Table (Already done in the above step)

# Step 3: Prepare for End User
# (Optional) Create views or additional operations based on your requirements.

# Example: Create a view for users older than 25
conn = mysql.connector.connect(**database_config)
cursor = conn.cursor()

create_view_query = '''
CREATE OR REPLACE VIEW mine AS
SELECT Name
FROM people;
'''
cursor.execute(create_view_query)

conn.commit()
conn.close()
