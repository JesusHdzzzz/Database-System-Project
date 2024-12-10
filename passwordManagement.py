import sqlite3
from sqlite3 import Error
import config
import datetime

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

        # Step 1: Print all groups the user has saved passwords for
        cursor.execute("""
            SELECT groups.group_name
            FROM groups
            JOIN group_pass ON groups.group_id = group_pass.group_id
            WHERE group_pass.user_id = ?
        """, (config.user_id,))
        
        groups = cursor.fetchall()

        # Check if the user belongs to any groups
        if not groups:
            print("You are not in any group.")
            return

        print("List of groups you have saved passwords for:")
        for row in groups:
            print(f"- {row[0]}")

        group_name = input("Enter the group name (case-sensitive): ").strip()

        # Step 2: Retrieve the password for the group
        cursor.execute("""
            SELECT group_email_pass 
            FROM group_pass
            WHERE user_id = ? AND group_id = (
                SELECT group_id FROM groups WHERE group_name = ?
            )
        """, (config.user_id, group_name))

        group_pass = cursor.fetchone()

        if group_pass:
            print(f"Group password for {config.username} in group {group_name}: {group_pass[0]}")
        else:
            print("No password found for the given user and group name.")

    except sqlite3.Error as e:
        print("Database error:", e)


"""
Retrieve passwords for both websites and groups for a specific user
"""
def retrievePassMenu(conn):
        
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

        # Add into history table
        cursor.execute("""
        INSERT INTO history (user_id, action_type, action_details, action_timestamp)
        VALUES (?, ?, ?, ?);
        """, (
            config.user_id,
            "Password change",
            f"Updated {website_name} password",
            datetime.datetime.now().strftime("%Y-%m-%d")
        ))

        conn.commit()
        print("Password updated successfully stored in History and Logs.")

    except sqlite3.Error as e:
        print("Database error: ", e)

def updateGroupPass(conn):
    try:
        cursor = conn.cursor()

        # Step 1: Retrieve groups the user belongs to
        cursor.execute("""
            SELECT groups.group_name
            FROM groups
            JOIN group_pass ON groups.group_id = group_pass.group_id
            WHERE group_pass.user_id = ?
        """, (config.user_id,))
        groups = cursor.fetchall()

        # Check if the user belongs to any groups
        if not groups:
            print("You are not in any group.")
            return

        print("List of groups you have saved passwords for:")
        for row in groups:
            print(f"- {row[0]}")

        # Ask for the group name to update the password
        group_name = input("Enter the group name (case-sensitive): ").strip()

        # Step 2: Check if the group exists
        cursor.execute("""
            SELECT group_id FROM groups WHERE group_name = ?
        """, (group_name,))
        group_row = cursor.fetchone()

        if not group_row:
            print(f"No group found with the name '{group_name}'.")
            return

        group_id = group_row[0]

        # Ask for the new password
        new_password = input("Enter the new password: ").strip()

        # Step 3: Update the password in group_pass table
        cursor.execute("""
            UPDATE group_pass
            SET group_email_pass = ?
            WHERE user_id = ? AND group_id = ?
        """, (new_password, config.user_id, group_id))

        # Insert into history table
        cursor.execute("""
            INSERT INTO history (user_id, action_type, action_details, action_timestamp)
            VALUES (?, ?, ?, ?)
        """, (
            config.user_id,
            "Password change",
            f"Updated password for group {group_name}",
            datetime.datetime.now().strftime("%Y-%m-%d")
        ))

        conn.commit()

        print("Password updated successfully and logged in history.")

    except sqlite3.Error as e:
        print("Database error:", e)


def updatePassMenu(conn):
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

        print("\nList of websites you have saved passwords for:")
        if saved_websites:
            for row in saved_websites:
                print(f"- {row[0]}")
        else:
            print("No websites saved yet.")

        # Get website details
        website_name = input("Enter the website name: ").strip().lower()
        website_url = input("Enter the website URL: ").strip()

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
                INSERT INTO web (website_name, website_url)
                VALUES (?, ?)
            """, (website_name, website_url))
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

        # Add into history table
        cursor.execute("""
        INSERT INTO history (user_id, action_type, action_details, action_timestamp)
        VALUES (?, ?, ?, ?);
        """, (
            config.user_id,
            "Password added",
            f"Added password for {website_name}",
            datetime.datetime.now().strftime("%Y-%m-%d")
        ))
        conn.commit()

        print("Password saved successfully stored in History and Logs.")

    except sqlite3.Error as e:
        print("Database error:", e)


def savePassMenu(conn):
    while True:
        print("\n|| Save a New Password ||")
        print("1. Save a new website password")
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

        # Add into history table
        cursor.execute("""
        INSERT INTO history (user_id, action_type, action_details, action_timestamp)
        VALUES (?, ?, ?, ?);
        """, (
            config.user_id,
            "Password deleted",
            f"Deleted password for {website_name}",
            datetime.datetime.now().strftime("%Y-%m-%d")
        ))
        conn.commit()

        # If the website exists, delete the password
        if result:
            website_id = result[0]
            cursor.execute("""
                DELETE FROM web_pass
                WHERE user_id = ? AND website_id = ?
            """, (config.user_id, website_id))
            conn.commit()
            print("Password deleted successfully and stored in History and Logs.")
        else:
            print("Website not found.")

        
    except sqlite3.Error as e:
        print("Database error:", e)

def deletePassMenu(conn):
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
    