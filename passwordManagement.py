import sqlite3
from sqlite3 import Error
import config

def retrieveWebPass(conn):
    try:
        cursor = conn.cursor()

        # Print all websites that the user has saved passwords for
        cursor.execute("""
            SELECT web.website_name
            FROM web
            JOIN web_pass ON web.website_id = web_pass.website_id
            WHERE web_pass.user_id = ?
            """, (config.user_id,))
        #print("config.user_id:", config.user_id)
        #print("config.username:", config.username)
        print("List of websites you have saved passwords for:")
        for row in cursor.fetchall():
            print(row[0])

        website_name = input("Enter the website name: ").strip().lower()

        cursor = conn.cursor()

        # Execute the query to retrieve the password for the given user and website
        cursor.execute("""SELECT web_pass 
            FROM web_pass, web
            WHERE user_id = ? 
            AND web_pass.website_id = web.website_id
            AND website_name = ?""", (config.user_id, website_name))
        web_pass = cursor.fetchone()

        # Check if a password was found and print it
        if web_pass:
            print(f"Website password for user {config.username} on website {website_name}: {web_pass[0]}")
        else:
            print("No password found for the given user ID and website name.")

    except sqlite3.Error as e:
        print("Database error: ", e)


def retrievePass(conn):
        
    while True:
        print("\nPassword Management")
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
        #try:
        #    all_pass = conn.execute("SELECT * FROM pass").fetchall()
    #
        #    if not all_pass:
        #        print("No passwords found.")
        #        return
    #
        #    print("List of all passwords:")
    #
        #    for row in all_pass:
        #        print(f"ID: {row[0]}, User ID: {row[1]}, Password: {row[2]}, Created At: {row[3]}")
        #        
        #except sqlite3.Error as e:
        #    print("Database error: ", e)
        
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