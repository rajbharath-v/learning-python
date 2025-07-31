import sqlite3
conn=sqlite3.connect('data.db')
print("the database is opened successfully ")
conn.execute("create table emp(sno int,sname text(20),dept text(10))")
print("table created successfully")
conn.close()