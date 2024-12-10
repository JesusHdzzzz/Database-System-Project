import config
import sqlite3

def viewPassHistory(conn):
    try:
        cursor = conn.cursor()

        # Execute query to get password history
        cursor.execute("""
            SELECT action_type, action_details, action_timestamp
            FROM history, users
            WHERE action_type LIKE "Password%"
            AND users.user_id = history.user_id
            AND history.user_id = ?;
        """, (config.user_id,))

        # Fetch all rows
        rows = cursor.fetchall()

        # Check if there's any history
        if not rows:
            print("You have no password history.")
            return

        # Print the password history
        print("Password History:")
        for row in rows:
            print(f"- {row[0]} | {row[1]} | {row[2]}")

    except sqlite3.Error as e:
        print("Database error:", e)


def viewCardHistory(conn):
    try:
        cursor = conn.cursor()

        # Execute query to get card history
        cursor.execute("""
            SELECT action_type, action_details, action_timestamp
            FROM history, users
            WHERE action_type LIKE "Card%"
            AND users.user_id = history.user_id
            AND history.user_id = ?;
        """, (config.user_id,))

        # Fetch all rows
        rows = cursor.fetchall()

        # Check if there's any history
        if not rows:
            print("You have no card history.")
            return

        # Print the card history
        print("Card History:")
        for row in rows:
            print(f"- {row[0]} | {row[1]} | {row[2]}")

    except sqlite3.Error as e:
        print("Database error:", e)