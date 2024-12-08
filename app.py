import sqlite3
from sqlite3 import Error
import re

def openConnection(_dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    return conn

def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def createTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create table")
    
    try:

        cur = _conn.cursor()

        cur.execute(""" 
            -- Users table (parent table)
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );""")
        
        cur.execute("""
        -- Passwords table
        CREATE TABLE IF NOT EXISTS pass (
            password_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INT,
            m_pass TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES Users(user_id) ON DELETE CASCADE
        );""")
        
        cur.execute("""
        -- Websites table
        CREATE TABLE IF NOT EXISTS web (
            website_id INTEGER PRIMARY KEY AUTOINCREMENT,
            website_name TEXT NOT NULL,
            website_url TEXT NOT NULL
        );""")
        
        cur.execute("""
        -- Web_passwords table
        CREATE TABLE IF NOT EXISTS web_pass (
            user_id INT,
            website_id INT,
            web_pass TEXT NOT NULL,
            PRIMARY KEY (user_id, website_id),
            FOREIGN KEY(user_id) REFERENCES Users(user_id) ON DELETE CASCADE,
            FOREIGN KEY(website_id) REFERENCES Websites(website_id) ON DELETE CASCADE
        );""")
        
        cur.execute("""
        -- CreditDebitCards table
        CREATE TABLE IF NOT EXISTS cards (
            card_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INT,
            cardholder_name TEXT NOT NULL,
            card_number TEXT NOT NULL,
            card_type TEXT NOT NULL CHECK (card_type IN ('Visa', 'MasterCard', 'American Express')),
            expiration_date TEXT NOT NULL,
            cvv TEXT NOT NULL,
            billing_address TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES Users(user_id) ON DELETE CASCADE
        );""")
        
        cur.execute("""
        -- History table
        CREATE TABLE IF NOT EXISTS history (
            history_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INT,
            action_type TEXT NOT NULL, 
            action_details TEXT,
            action_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES Users(user_id) ON DELETE CASCADE
        );""")
        
        cur.execute("""
        -- DevicesLocations table
        CREATE TABLE IF NOT EXISTS devloc (
            entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INT,
            device_name TEXT,
            device_type TEXT,
            operating_system TEXT,
            ip_address TEXT,
            city TEXT,
            country TEXT,
            login_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES Users(user_id) ON DELETE CASCADE
        );""")
        
        cur.execute("""
        -- Groups table
        CREATE TABLE IF NOT EXISTS groups (
            group_id INTEGER PRIMARY KEY AUTOINCREMENT,
            group_name TEXT NOT NULL,
            group_domain TEXT NOT NULL,
            group_type TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );""")
        
        cur.execute("""
        -- Group_Users table
        CREATE TABLE IF NOT EXISTS group_u (
            group_id INTEGER,
            user_id INTEGER,
            email TEXT NOT NULL,
            PRIMARY KEY (group_id, user_id),
            FOREIGN KEY(group_id) REFERENCES Groups(group_id) ON DELETE CASCADE,
            FOREIGN KEY(user_id) REFERENCES Users(user_id) ON DELETE CASCADE
        );""")
        
        cur.execute("""
        -- Group_Passwords table
        CREATE TABLE IF NOT EXISTS group_link (
            group_id INTEGER,
            password_id INTEGER,
            PRIMARY KEY (group_id, password_id),
            FOREIGN KEY(group_id) REFERENCES Groups(group_id) ON DELETE CASCADE,
            FOREIGN KEY(password_id) REFERENCES Passwords(password_id) ON DELETE CASCADE
        );""")
        
        cur.execute("""
        -- User_Websites table
        CREATE TABLE IF NOT EXISTS user_web (
            user_id INT,
            website_id INT,
            PRIMARY KEY (user_id, website_id),
            FOREIGN KEY(user_id) REFERENCES Users(user_id) ON DELETE CASCADE,
            FOREIGN KEY(website_id) REFERENCES Websites(website_id) ON DELETE CASCADE
        );""")
        
        cur.execute("""
        CREATE TABLE IF NOT EXISTS group_pass (
            group_id INTEGER, -- References the group the user belongs to
            user_id INTEGER, -- References the user within the group
            group_email_pass TEXT NOT NULL, -- Stores the password for the user's group email
            PRIMARY KEY (group_id, user_id), -- Composite primary key ensures unique group-user-password relationship
            FOREIGN KEY (group_id) REFERENCES groups(group_id) ON DELETE CASCADE, -- Cascade delete when a group is deleted
            FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Cascade delete when a user is deleted
        );""")
        _conn.commit()
        print("success")    
    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


# def dropTable(_conn):
#     print("++++++++++++++++++++++++++++++++++")
#     print("Drop tables")
    
#     #cur = _conn.cursor()
#     try:
#         sql= "DROP TABLE warehouse"
#         _conn.execute(sql)
        
#         _conn.commit()
#         print("success")
        
#     except Error as e:
#         _conn.rollback()
#         print(e)
    
#     print("++++++++++++++++++++++++++++++++++")
# 

def createAccount(conn):
    # Step 1: Get Email from the User and Validate It
    while True:
        email = input("Enter your email address: ").strip()

        # Validate email format
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("Invalid email format. Please try again.")
            continue
        
        try:
            # Check if the email already exists in the database
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
            if cursor.fetchone():
                print("Email already exists. Please try a different email.")
                continue

            break  # Email is valid and doesn't already exist

        except sqlite3.Error as e:
            print("Database error while checking email: ", e)

    # Step 2: Get the Username
    while True:
        username = input("Enter a new username: ").strip()

        try:
            # Insert the new user into the database
            conn.execute("INSERT INTO users (username, email) VALUES (?, ?)", (username, email))
            conn.commit()
            print(f"Username '{username}' successfully added to the database.")
            break
        except sqlite3.IntegrityError:
            print("Username already exists. Please try a different username.")

    # Step 3: Get the Master Password
    while True:
        m_pass = input("Create a master password: ").strip()

        if len(m_pass) < 6:
            print("Your password must be at least 6 characters long.")
            continue

        try:
            cursor = conn.cursor()

            # Retrieve user_id for the newly created username
            cursor.execute("SELECT user_id FROM users WHERE username = ?", (username,))
            user_id = cursor.fetchone()[0]

            # Save the master password in the `pass` table
            conn.execute("INSERT INTO pass (user_id, m_pass) VALUES (?, ?)", (user_id, m_pass))
            conn.commit()

            print("Account successfully created with a master password.")
            return True
            break
        except sqlite3.Error as e:
            print("Database error while creating password: ", e)

def login(conn):
    """Handles user login."""
    try:
        username = input("Enter your username: ").strip()
        cursor = conn.cursor()

        # Query to fetch the user's stored password based on the username
        query = """
            SELECT pass.m_pass 
            FROM users 
            JOIN pass ON users.user_id = pass.user_id 
            WHERE users.username = ?
        """
        cursor.execute(query, (username,))
        user = cursor.fetchone()

        print("Username supplied:", username)
        print("Is it a tuple?", isinstance((username,), tuple))


        if user:
            # User found; prompt for password
            stored_password = user[0]  # Extract stored password from the query result
            password = input("Enter your password: ").strip()

            if password == stored_password:
                print("Login successful!")
                return True
            else:
                print("Incorrect password. Please try again.")
        else:
            # User not found
            print("Username does not exist. Please try again.")
    except sqlite3.Error as e:
        print("Database error: ", e)
    except Exception as e:
        print("Unexpected error: ", e)



def main():
    database = r"Checkpoint2-dbase.db"
    # create a database connection
    conn = openConnection(database)
    #createTable(conn)
    
    while True:
        print("1. Log in")
        print("2. Create a new account")

        choice = input("Enter your choice: ")

        if choice == '1':
            if login(conn):
                break
        elif choice == '2':
            if createAccount(conn):
                break
        else:
            print("Invalid choice. Please try again.")

    
    while True:
        print("\nPassword Manager")
        print("1. Add User")
        print("2. Add Website")
        print("3. Save Password")
        print("4. Retrieve Password")
        print("5. Exit")
        choice = input("Enter your choice: ")

    closeConnection(conn, database)


if __name__ == '__main__':
    main()
