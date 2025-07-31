import sqlite3
db=sqlite3.connect('test.db')
qry="insert into secsk(id,name, age) values(?,?,?);"
students=[(12,'welcome', 18), (13,'Deepak', 25)]
try:
    cur=db.cursor()
    cur.executemany(qry, students)
    db.commit()
    print ("records added successfully")
except:
    print ("error in operation")
    db.rollback()
db.close()
