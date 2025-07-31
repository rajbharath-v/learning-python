import sqlite3
conn=sqlite3.connect('data.db')
qry="insert into emp(sno,sname,dept) values(?,?,?);"
companyemp=[(2,'ravon','CSE'),
        (3,'sai','CSE'),
        (4,'kiran','CSE'),
        (5,'suresh','CSE')]
try:
    raj=conn.cursor()
    raj.executemany(qry,companyem p)
    conn.commit()
    print("table value is inserted ")
except:
    print("the value is not inserted may be the value is not proper")
    conn.rollback()
conn.close()