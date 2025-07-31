import sqlite3
conn=sqlite3.connect('data.db')
qry="insert into emp(sno,sname,dept) values(1,'Raj','CSE');"
try:
    raj=conn.cursor()
    raj.execute(qry)
    conn.commit()
    print("the vlaue is inserted in the table")
except:
    print("the value is not inserted may be the value is not proper")
    conn.rollback()
conn.close()
