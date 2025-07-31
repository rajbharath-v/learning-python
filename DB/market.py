import sqlite3
def create():
    con=sqlite3.connect('supermarket.db')
    cur=con.cursor()
    cur.execute('''  CREATE TABLE IF NOT EXISTS customer(
                c_id  INTEGER PRIMARY KEY AUTOINCREMENT,
                c_name TEXT NOT NULL,
                c_address TEXT NOT NULL,
                c_phoneno INTEGER NOT NULL
                )
    ''' )
    con.commit()
    con.close()
def add_cus(name,address,phoneno):
    con=sqlite3.connect('supermarket.db')
    cur=con.cursor()
    try:
        cur.execute("insert into  customer(c_name,c_address,c_phoneno) values(?,?,?)",(name,address,phoneno))
        print("successfully added")
        con.commit()
        print()
    except sqlite3.IntegrityError:
        print("error")
    con.close()
def view():
    con=sqlite3.connect('supermarket.db')
    cur=con.cursor()
    cur.excute("SELECT *FROM customer")
    rows=cur.fetchall()
    print("---user list---")
    for row in rows:
        print(f"id:{row[0]},name:{row[1]},address:{row[2]},phoneno:{row[3]}")
    con.close()
def update(c_id,c_name,c_address,c_phoneno):
    con=sqlite3.connect('supermarket.db')
    cur=con.cursor()
    cur.execute("update customer set c_name=?,c_address=?,c_phoneno=? where c_id=?",(c_name,c_address,c_phoneno,c_id))
    if cur.rowcount == 0:
        print("User not found.")
    else:
        print("User updated successfully.")
    con.commit()
    con.close()
def delete(c_id):
    con=sqlite3.connect('supermarket.db')
    cur=con.cursor()
    cur.execute("delete from customer sher id=?",(c_id))
    if cur.rowcount==0:
        print("the user not found")
    else:
        print("the user id is successfuly deleted")
    con.commit()
    con.close()



def main():
   create()
   print("supermarketbilling")
   print("1.add the new customer")
   print("2.view the customer")
   print("3.update the customer details")
   print("4.delete the customer")
   print("5.exit")
   choice=input("enter the choice :") 
   if choice=='1':
       name=input("enter the customer name:")
       address=input("enter the address of customer")
       phoneno=int(input("enter the customer phoneno"))
       add_cus(name,address,phoneno)

   elif choice=='2':
       view()
   elif choice=='3':
       try:
           c_id=int(input("enter the customer id"))
           c_name=input("enter the custumer name")
           c_address=input("enter the address of the customer")
           c_phoneno=int(input("enter the customer phoneno"))
           update(c_id,c_name,c_address,c_phoneno)
       except ValueError:
           print("type errpr of id is not matching")  
   elif choice=='4':
        try:
           c_id = int(input("Enter user ID to delete: "))
           delete(c_id)
        except ValueError:
                print("Invalid input. ID must be a number.")
   elif choice=='5':
       print("exiting the program")
       breakpoint
   else:
       print("invalid")
if __name__ == "__main__":
    main()