#SQL adding stuffs

import sqlite3

conn = sqlite3.connect("mydb.db")

c = conn.cursor()

#Usually yopur SQL operations will need to use values from Python vairables.
#You shouldn't assemble your query using Python's string operations because doing so
#is insecure: SQL injection attacks

#Larger example that inserst many records at once
mypeople = [('Sam', 'Jones', '18'),
            ('Lisa', 'Taylor', '19'),
            ('Kay', 'Johnson', '20'),
            ]

c.executemany ('INSERT INTO people1 VALUES (?, ?, ?)', mypeople)

#Saves change
conn.commit()

#Fetches all from database
c.execute("SELECT * FROM people1")

print("Fetchall: ")

result = c.fetchall()

for r in result:
    print (r)
#fetches all qith forename beginning with S

c.execute("SELECT * FROM people1 WHERE forename like 'S%' ")

print("fetch: ")

result = c.fetchall()
for s in result:
    print(s)

#school = # select * from course where name like 'Algebra%';

#c.close()
