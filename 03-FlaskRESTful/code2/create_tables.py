import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

# for autoincrementing columns you need INTEGER otherwise int is ok
create_table = "CREATE TABLE users (id INTEGER PRIMARY KEY, username text, password text)"
try:
    cursor.execute(create_table)
except:
    print("didnt create the table")

connection.commit()

connection.close()