def viewPassHistory(conn):
  try:
    cursor = conn.cursor()

    # Print all websites that the user has saved passwords for
    cursor.execute("""
        SELECT action_type, action_details, action_timestamp
        FROM history
        WHERE action_type LIKE "Password%"
        AND history.user_id = ?
        """, (config.user_id,))
    #print("config.user_id:", config.user_id)
    #print("config.username:", config.username)


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
  



def viewCardHistory(conn):