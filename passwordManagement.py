import sqlite3
from sqlite3 import Error

def retrievePass(conn):
        
    while True:
        print("1. Retrieve a website password")
        print("2. Retrieve a group password")
        print("3. Retrieve all passwords")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            retrieveWebPass(conn)
        elif choice == '2':
            retrieveGroupPass(conn)
        elif choice == '3':
            retrieveAllPass(conn)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
        try:
            all_pass = conn.execute("SELECT * FROM pass").fetchall()
    
            if not all_pass:
                print("No passwords found.")
                return
    
            print("List of all passwords:")
    
            for row in all_pass:
                print(f"ID: {row[0]}, User ID: {row[1]}, Password: {row[2]}, Created At: {row[3]}")
                
        except sqlite3.Error as e:
            print("Database error: ", e)
        
#def updatePass(conn):
#    try:
#
#    except sqlite3.Error as e:
#        print("Database error: ", e)
#        
#def savePass(conn):
#    try:
#
#    except sqlite3.Error as e:
#        print("Database error: ", e)
#        
#def viewPassHistory(conn):
#    try:
#
#    except sqlite3.Error as e:
#        print("Database error: ", e)