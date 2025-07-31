import sqlite3
def create():
    
    con=sqlite3.connect('bank.db')
    cur=con.curser()
    cur.execute(''''create table IF NOT EXITS ATM(
                c_id  INTEGER AUTOINCREMENT,
                accno int primary key,
                name text not null,
                address text,pin=1234
                
    )  ''')
def create1():
    con=sqlite3.connect('bank.db')
    cur=con.cursor()
    try:
        cur.execute('''insert into atm(accno,name,address) values(?,?,?),(acc)''')
def main():
    create()
    print("----ATM MANAGEMENT SYSTEM----")
    print("1.create the account number to the atm by the bank")
    print("2.view the no of user in the atm")
    print("3.change the details of users")
    print("4.delete the details")
    print("5.exit")
    choice=int(input("enter the choice where given in the upper(1 to 5)"))
    if choice<=5:
        if choice=='1':
            accno=int(input("enter the accno"))
            name=input("enter the name")
            address=input("enter the address")
            pinno=int(input("enter the pin no"))
            if pinno==pin:
                con=sqlite3.connect('bank.db')
                cur=con.cursor()
                cur.execute("insert into ATM values(?,?,?)",(accno,name,address))
                print("account created successfully")
                con.commit()
                con.close()
            else:
                print("invalid pin")
        elif choice=='2':
            con=sqlite3.connect('bank.db')
            cur=con.cursor()
            cur.execute("select * from ATM")
            rows=cur.fetchall()
            print("----user list----")
            for row in rows:
                print(f"accno:{row[0]},name:{row[1]},address:{row[2]}")
            con.close()
        elif choice=='3':
            con=sqlite3.connect('bank.db')
            cur=con.cursor()
            accno=int(input("enter the accno to update"))
            name=input("enter the name")
            address=input("enter the address")
            pinno=int(input("enter the pin no"))
            if pinno==pin:
                cur.execute("update ATM set name=?,address=? where accno=?",(name,address,accno))
                print("user details updated successfully")
                con.commit()
                con.close()
            else:
                print("invalid pin")
        elif choice=='4':
            con=sqlite3.connect('bank.db')
            cur=con.cursor()
            accno=int(input("enter the accno to delete"))
            pinno=int(input("enter the pin no"))
            if pinno==pin:
                cur.execute("delete from ATM where accno=?",(accno,))
                print("user details deleted successfully")
                con.commit()
                con.close()
            else:
                print("invalid pin")
        elif choice=='5':
            print("thank you for using the ATM management system")
    else:
        print("invalid choice")
             

