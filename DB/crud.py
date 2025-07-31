import sqlite3
def create_table():
    conn = sqlite3.connect('crud.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def create_user(name, email):
    conn = sqlite3.connect('crud.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        print("User added successfully.")
    except sqlite3.IntegrityError:
        print("Error: Email already exists.")
    conn.close()

def read_users():
    conn = sqlite3.connect('crud.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    print("\n--- User List ---")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")
    conn.close()
def update_user(user_id, new_name, new_email):
    conn = sqlite3.connect('crud.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (new_name, new_email, user_id))
    if cursor.rowcount == 0:
        print("User not found.")
    else:
        print("User updated successfully.")
    conn.commit()
    conn.close()

def delete_user(user_id):
    conn = sqlite3.connect('crud.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    if cursor.rowcount == 0:
        print("User not found.")
    else:
        print("User deleted successfully.")
    conn.commit()
    conn.close()

def main():
    create_table()
    while True:
        print("\n====== User Management System ======")
        print("1. Add User")
        print("2. View Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            create_user(name, email)
        elif choice == '2':
            read_users()
        elif choice == '3':
            try:
                user_id = int(input("Enter user ID to update: "))
                new_name = input("Enter new name: ")
                new_email = input("Enter new email: ")
                update_user(user_id, new_name, new_email)
            except ValueError:
                print("Invalid input. ID must be a number.")
        elif choice == '4':
            try:
                user_id = int(input("Enter user ID to delete: "))
                delete_user(user_id)
            except ValueError:
                print("Invalid input. ID must be a number.")
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()