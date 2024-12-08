import sqlite3
from sqlite3 import Error
from create_tables import createTable
import re
import config
from passwordManagement import *
from creditDebitCardMan import *
from groupEmail import *
from history import *

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
            print("You can now log in with your username and password.")
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
        print('\n|| Password Management ||')
        print("1. Retrieve a website/group password")
        # Done.
        print("2. Update a website/group password")
        # Done.
        print("3. Save a new password for website/group")
        # WIP.
        print("4. Delete a website or grouppassword")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            retrievePass(conn)
        if choice == '2':
            updatePass(conn)
        if choice == '3':
            savePass(conn)
        if choice == '4':
            deletePass(conn)
        if choice == '5':
            break

def cardManage(conn):
    while True:
        print('\n|| Credit/Debit Card Management ||')
        print("1. Add a new credit/debit card")
        # Done.
        print("2. Delete a credit/debit card")
        # Done.
        print("3. Update a credit/debit card")
        # Done.
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            addCard(conn)
        if choice == '2':
            deleteCard(conn)
        if choice == '3':
            updateCard(conn)
        if choice == '4':
            break

def gEmail(conn):
    while True:
        print('\n|| Group and Email Integration ||')
        print("1. Retrieve group emails")
        # Done.
        print("2. Update group emails")
        # Done.
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            retrieveEmail(conn)
        if choice == '2':
            updateEmail(conn)
        if choice == '3':
            break

def history(conn):
    while True:
        print('\n|| History and Logs ||')
        print("1. View password history")
        # Done.
        print("2. View credit/debit card history")
        # Done.
        print("3. View group email history")
        # Done.
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            viewPassHistory(conn)
        if choice == '2':
            viewCardHistory(conn)
        if choice == '3':
            viewEmailHistory(conn)
        if choice == '4':
            break

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
        print("1. Password and Website Management")
        # Retrieve, save, delete, update passwords
        print("2. Credit/Debit Card Management")
        # Add a new credit card, delete a credit card, update a credit card
        print("3. Group and Email Integration")
        # Retrieve and update group emails only
        print("4. History and Logs")
        # Retrieve change history
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            passManage(conn)
        if choice == '2':
            cardManage(conn)
        if choice == '3':
            gEmail(conn)
        if choice == '4':
            history(conn)
        if choice == '5':
            config.username = None
            config.user_id = None
            closeConnection(conn, database)
            break

if __name__ == '__main__':
    main()
