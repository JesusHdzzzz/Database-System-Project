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
            print(f"- {row[0]}")

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

def retrieveGroupPass(conn):
    try:
        cursor = conn.cursor()

        # Print all groups that the user has saved passwords for
        cursor.execute("""
            SELECT groups.group_name
            FROM groups
            JOIN group_pass ON groups.group_id = group_pass.group_id
            WHERE group_pass.user_id = ?
            """, (config.user_id,))
        print("List of groups you have saved passwords for:")
        for row in cursor.fetchall():
            print(f"- {row[0]}")

        group_name = input("Enter the group name (case-sensitive): ").strip()

        cursor = conn.cursor()

        # Execute the query to retrieve the password for the given user and group
        cursor.execute("""SELECT group_email_pass 
            FROM group_pass, groups
            WHERE user_id = ? 
            AND group_pass.group_id = groups.group_id
            AND group_name = ?""", (config.user_id, group_name))
        group_pass = cursor.fetchone()

        print("config.user_id:", config.user_id)
        print("group_name:", group_name)

        # Check if a password was found and print it
        if group_pass:    
            print(f"Group password for user {config.username} in group {group_name}: {group_pass[0]}")
        else:
            print("No password found for the given user ID and group name.")

    except sqlite3.Error as e:
        print("Database error: ", e)

"""
Retrieve passwords for both websites and groups for a specific user
"""
def retrievePass(conn):
        
    while True:
        print("\n|| Retrieve a Password ||")
        print("1. Retrieve a website password")
        # Done.
        print("2. Retrieve a group password")
        # Done.
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            retrieveWebPass(conn)
        elif choice == '2':
            retrieveGroupPass(conn)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def updateWebPass(conn):
    try:
        cursor = conn.cursor()

        # Print all websites that the user has saved passwords for
        cursor.execute("""
            SELECT web.website_name
            FROM web
            JOIN web_pass ON web.website_id = web_pass.website_id
            WHERE web_pass.user_id = ?
            """, (config.user_id,))
        print("List of websites you have saved passwords for:")
        for row in cursor.fetchall():
            print(f"- {row[0]}")

        website_name = input("Enter the website name: ").strip().lower()

        cursor = conn.cursor()

        # Execute the query to update the password for the given user and website
        cursor.execute("""
            UPDATE web_pass
            SET web_pass = ?
            WHERE user_id = ?
            AND website_id = (
                SELECT website_id
                FROM web
                WHERE website_name = ?
            )
            """, (input("Enter the new password: "), config.user_id, website_name))

        conn.commit()
        print("Password updated successfully.")

    except sqlite3.Error as e:
        print("Database error: ", e)

def updateGroupPass(conn):
    try:
        cursor = conn.cursor()

        # Print all groups that the user has saved passwords for
        cursor.execute("""
            SELECT groups.group_name
            FROM groups
            JOIN group_pass ON groups.group_id = group_pass.group_id
            WHERE group_pass.user_id = ?
            """, (config.user_id,))
        print("List of groups you have saved passwords for:")
        for row in cursor.fetchall():
            print(f"- {row[0]}")

        group_name = input("Enter the group name (case-sensitive): ").strip()

        cursor = conn.cursor()

        # Execute the query to update the password for the given user and group
        cursor.execute("""
            UPDATE group_pass
            SET group_email_pass = ?
            WHERE user_id = ?
            AND group_id = (
                SELECT group_id
                FROM groups
                WHERE group_name = ?
            )
            """, (input("Enter the new password: "), config.user_id, group_name))

        conn.commit()
        print("Password updated successfully.")

    except sqlite3.Error as e:
        print("Database error: ", e)

def updatePass(conn):
    while True:
        print("\n|| Password Management ||")
        print("1. Update a website password")
        # Done.
        print("2. Update a group password")
        # Done.
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            updateWebPass(conn)
        elif choice == '2':
            updateGroupPass(conn)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def saveWebPass(conn):
    try:
        cursor = conn.cursor()

        # Print all websites the user has saved passwords for
        cursor.execute("""
            SELECT web.website_name
            FROM web
            JOIN web_pass ON web.website_id = web_pass.website_id
            WHERE web_pass.user_id = ?
        """, (config.user_id,))
        saved_websites = cursor.fetchall()

        print("List of websites you have saved passwords for:")
        if saved_websites:
            for row in saved_websites:
                print(f"- {row[0]}")
        else:
            print("No websites saved yet.")

        # Get website details
        website_name = input("Enter the website name: ").strip().lower()

        # Check if the website exists
        cursor.execute("""
            SELECT website_id
            FROM web
            WHERE website_name = ?
        """, (website_name,))
        result = cursor.fetchone()

        if result:
            website_id = result[0]  # Existing website_id
        else:
            # Insert new website
            cursor.execute("""
                INSERT INTO web (website_name)
                VALUES (?)
            """, (website_name,))
            conn.commit()
            website_id = cursor.lastrowid  # New website_id

        # Check for existing password entry
        cursor.execute("""
            SELECT 1
            FROM web_pass
            WHERE user_id = ? AND website_id = ?
        """, (config.user_id, website_id))

        if cursor.fetchone():
            print("A password for this website already exists. Use the update option to modify it.")
            return

        # Insert the password for the website
        web_pass = input("Enter the password: ").strip()
        cursor.execute("""
            INSERT INTO web_pass (user_id, website_id, web_pass)
            VALUES (?, ?, ?)
        """, (config.user_id, website_id, web_pass))
        conn.commit()

        print("Password saved successfully.")

    except sqlite3.Error as e:
        print("Database error:", e)


def savePass(conn):
    while True:
        print("\n|| Save a New Password ||")
        print("1. Save a new website and website password")
        print("2. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            saveWebPass(conn)
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please try again.")

def deleteWebPass(conn):
    try:
        cursor = conn.cursor()
        # Print all websites the user has saved passwords for        
        # Print all websites the user has saved passwords for
        cursor.execute("""
            SELECT web.website_name
            FROM web
            JOIN web_pass ON web.website_id = web_pass.website_id
            WHERE web_pass.user_id = ?
        """, (config.user_id,))
        saved_websites = cursor.fetchall()

        print("List of websites you have saved passwords for:")
        if saved_websites:
            for row in saved_websites:
                print(f"- {row[0]}")
        else:
            print("No websites saved yet.")

        # Get website details
        website_name = input("Enter the website name: ").strip().lower()

        # Check if the website exists
        cursor.execute("""
            SELECT website_id
            FROM web
            WHERE website_name = ?
        """, (website_name,))
        result = cursor.fetchone()

        print(result)
        
    except sqlite3.Error as e:
        print("Database error:", e)

def deletePass(conn):
    while True:
        print("\n|| Delete a Password ||")
        print("1. Delete a website password")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            deleteWebPass(conn)
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please try again.")