import sqlite3
from sqlite3 import Error
<<<<<<< HEAD
import getpass

=======
from create_tables import createTable
import re
from passwordManagement import *
import config
>>>>>>> 8873dbb10089f142feb8255b3c1d25d046a0f91e

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

def createAccount(conn):
<<<<<<< HEAD
    try:
        # Step 1: Gather user details
        username = input("Enter your username: ")
        email = input("Enter your email address: ")

        # Step 2: Insert user into the Users table
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, email) VALUES (?, ?)", 
            (username, email)
        )
        conn.commit()

        # Fetch the user_id of the newly created user
        user_id = cursor.lastrowid

        # Step 3: Prompt for master password
        print("Set a master password for your account (you'll use this to access your data).")
        master_password = getpass.getpass("Enter your master password: ")
        confirm_password = getpass.getpass("Confirm your master password: ")

        if master_password != confirm_password:
            print("Passwords do not match. Please try again.")
            conn.execute("DELETE FROM Users WHERE user_id = ?", (user_id,))
            conn.commit()
            return

        # Step 4: Save the master password in the pass table
        cursor.execute(
            "INSERT INTO pass (user_id, m_pass) VALUES (?, ?)", 
            (user_id, master_password)
        )
        conn.commit()

        print(f"Account for '{username}' created successfully!")

    except sqlite3.IntegrityError as e:
        if "UNIQUE constraint failed: Users.username" in str(e):
            print("Username is already taken. Please choose a different username.")
        elif "UNIQUE constraint failed: Users.email" in str(e):
            print("Email is already registered. Please use a different email address.")
        else:
            print("An error occurred:", e)


=======
    # Step 1: Get Email from the User and Validate It
    while True:
        email = input("Enter your email address: ").strip()

        # Validate email format
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("Invalid email format. Please try again.")
            continue
>>>>>>> 8873dbb10089f142feb8255b3c1d25d046a0f91e
        
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
<<<<<<< HEAD
    username = input("Enter your username: ")
    master_password = getpass.getpass("Enter your master password: ")

    try:
        # Step 1: Check if the username exists
        cursor = conn.cursor()
        cursor.execute(
            "SELECT u.user_id, p.m_pass FROM users u "
            "JOIN pass p ON u.user_id = p.user_id "
            "WHERE u.username = ?",
            (username,)
        )
        result = cursor.fetchone()

        if result is None:
            print("Invalid username or password. Please try again.")
            return None

        user_id, stored_password = result

        # Step 2: Validate the master password
        if master_password == stored_password:
            print(f"Login successful! Welcome, {username}.")
            return user_id  # Return user_id for further operations
        else:
            print("Invalid username or password. Please try again.")
            return None

    except sqlite3.Error as e:
        print("An error occurred:", e)
        return None
=======
    """Handles user login."""
    try:
        username = input("Enter your username: ").strip()
        cursor = conn.cursor()

        # Query to fetch the user's stored password based on the username
        query = """
            SELECT pass.m_pass, users.user_id
            FROM users 
            JOIN pass ON users.user_id = pass.user_id 
            WHERE users.username = ?
        """
        cursor.execute(query, (username,))
        user = cursor.fetchone()

        #print("Username supplied:", username)
        #print("Is it a tuple?", isinstance((username,), tuple))

        if user:
            # User found; prompt for password
            stored_password = user[0]  # Extract stored password from the query result
            password = input("Enter your password: ").strip()

            if password == stored_password:
                config.username = username # Set the global variable for username
                config.user_id = user[1] # Set the global variable for user_id

                #print("User ID:", config.user_id)
                #print("Username:", config.username)

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

def passManage(conn):
    while True:
        print('\nPassword Management')
        print("1. Retrieve a website/group password")
        print("2. Update a website/group password")
        print("3. Save a new password for website/group")
        print("4. View password history")

        choice = input("Enter your choice: ")

        if choice == '1':
            retrievePass(conn)
        if choice == '2':
            updatePass(conn)
        if choice == '3':
            savePass(conn)
        if choice == '4':
            viewPassHistory(conn)
>>>>>>> 8873dbb10089f142feb8255b3c1d25d046a0f91e


def main():
    database = r"Checkpoint2-dbase.db"
    # create a database connection
    conn = openConnection(database)
    #createTable(conn)
    
    if conn:
        createTable(conn)
        print("Tables are ready to use.")

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
        print("\n|| Password Manager ||")
        print("1. Password Management")
        print("2. Website Management")
        print("3. Credit/Debit Card Management")
        print("4. Group and Email Integration")
        print("5. History and Logs")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            passManage(conn)
        if choice == '2':
            webManage(conn)
        if choice == '3':
            cdMan(conn)
        if choice == '4':
            gEmail(conn)
        if choice == '5':
            history(conn)
        if choice == '6':
            config.username = None
            closeConnection(conn, database)

if __name__ == '__main__':
    main()
