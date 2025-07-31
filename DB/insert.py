import sqlite3
db=sqlite3.connect('test.db')
qry="insert into Secsk(id, name,age) values(13,'Raj', 44);"
try:
    cur=db.cursor()
    cur.execute(qry)
    db.commit()
    print ("one record added successfully")
except:
    print ("error in operation")
    db.rollback()
db.close()
