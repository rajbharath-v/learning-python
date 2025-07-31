import sqlite3
db = sqlite3.connect('db2.db')
qry="into table student(sno ,sname ,dept) values(1,'Raj','CSE');" 
print("the database is opened successfully ")
try:
    cur=db.cursor()
    cur.execute(qry)
    db.commit()
except:
    print("enter the correct value ")
    db.rollback()
db.close()