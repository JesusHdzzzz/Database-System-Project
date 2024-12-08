import config
import sqlite3
def viewPassHistory(conn):
  try:
    cursor = conn.cursor()

    # Print all websites that the user has saved passwords for
    cursor.execute("""
        SELECT action_type, action_details, action_timestamp
        FROM history, users
        WHERE action_type LIKE "Password%"
        AND users.user_id = history.user_id
        AND history.user_id = ?;
        """, (config.user_id,))
    #print("config.user_id:", config.user_id)
    #print("config.username:", config.username)
    for row in cursor.fetchall():
            print(f"- {row[0]} | {row[1]} | {row[2]}")


  except sqlite3.Error as e:
    print("Database error: ", e)

def viewCardHistory(conn):
    try:
        cursor = conn.cursor()

        # Print all websites that the user has saved passwords for
        cursor.execute("""
            SELECT action_type, action_details, action_timestamp
        FROM history, users
        WHERE action_type LIKE "Card%"
        AND users.user_id = history.user_id
        AND history.user_id = ?;
            """, (config.user_id,))
        #print("config.user_id:", config.user_id)
        #print("config.username:", config.username)
        for row in cursor.fetchall():
            print(f"- {row[0]} | {row[1]} | {row[2]}")
            
    except sqlite3.Error as e:
        print("Database error: ", e)
   