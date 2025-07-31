
import sqlite3
conn = sqlite3.connect('test.db')
print ("Opened database successfully")

conn.execute("create table Secsk(id int,name text , age int);")
print ("Table created successfully")

conn.close()

'''
import sqlite3
db=sqlite3.connect('test.db')
try:        
    cur =db.cursor()
    cur.execute("create table Goods(sno int,sname text(20))")
    print ('table created successfully')
except:
    print ('error in operation')
    db.rollback()
db.close()



'''

