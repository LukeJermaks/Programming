#SQL stuffs

import sqlite3

#Connection object to represent database
conn = sqlite3.connect("mydb.db")

#Cursor object and call execute method
c = conn.cursor()

#Creates table
c.execute('''CREATE TABLE people1 (forename text, surname text, age int)''')

#Inserts into table
c.execute("INSERT INTO people1 VALUES ('Bob', 'Smith', '16')")

#Saves change
conn.commit()
