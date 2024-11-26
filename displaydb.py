import sqlite3
from prettytable import PrettyTable

# Connect to the database
conn = sqlite3.connect('users1.db')
cursor = conn.cursor()

# Execute a query to fetch email and role
cursor.execute("SELECT email, role FROM user")

# Fetch all results
rows = cursor.fetchall()

# Create a PrettyTable instance
table = PrettyTable()
table.field_names = ["Email", "Role"]

# Add rows to the table
for row in rows:
    table.add_row(row)

# Print the table
print(table)

# Close the connection
conn.close()
