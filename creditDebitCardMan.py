import sqlite3
from sqlite3 import Error
import config
import datetime

def retrieveCard(conn):
    try:
        cursor = conn.cursor()

        # Query to retrieve all card details
        cursor.execute("""
            SELECT cardholder_name, card_number, card_type, expiration_date, billing_address
            FROM cards
            WHERE user_id = ?;
        """, (config.user_id,))

        # Save the results from fetchall() into a variable
        cards = cursor.fetchall()

        # Let user know if they have no cards
        if not cards:
            print("\nYou have no saved cards.")
            return

        # Print all card details
        print("Your saved credit/debit cards:")
        for row in cards:
            print(f"- {row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")

    except sqlite3.Error as e:
        print("Database error:", e)


def addCard(conn):
    try:
        
        """
        # print current year
        print("Current year:", datetime.datetime.now().year)
        cursor = conn.cursor()

        # print current month
        print("Current month:", datetime.datetime.now().month)
        """

        # Gather card details
        cardholder_name = input("Enter cardholder name: ").strip()
        card_number = input("Enter card number (16 digits): ").strip()

        # Check if card number alredy exists
        cursor = conn.cursor()
        cursor.execute("SELECT card_number FROM cards WHERE card_number = ?", (card_number,))
        existing_card = cursor.fetchone()

        if existing_card:
            print("\nCard number already exists. Please try again.")
            return

        # Validate card number
        if not card_number.isdigit() or len(card_number) != 16:
            print("\nInvalid card number. Please try again.")
            return

        card_type = input("Enter card type ('Visa', 'MasterCard', 'American Express' Only): ").strip()

        # Validate card type
        if card_type not in ['Visa', 'MasterCard', 'American Express']:
            print("\nInvalid card type. Please try again.")
            return

        expiration_date = input("Enter expiration date (YYYY-MM): ").strip()

        # Validate expiration date and that it expires in the future
        if not expiration_date.isdigit() and len(expiration_date) != 7 and (expiration_date[:4]) <= str(datetime.datetime.now().year) and (expiration_date[5:]) <= str(datetime.datetime.now().month):
            print("\nInvalid or expired expiration date. Please try again.")
            return

        billing_address = input("Enter billing address: ").strip()

        # Insert the card into the database
        cursor.execute("""
            INSERT INTO cards (cardholder_name, card_number, card_type, expiration_date, billing_address, user_id)
            VALUES (?, ?, ?, ?, ?, ?);
        """, (cardholder_name, card_number, card_type, expiration_date, billing_address, config.user_id))

        # Commit the transaction
        conn.commit()

        # Add into history table
        cursor.execute("""
        INSERT INTO history (user_id, action_type, action_details, action_timestamp)
        VALUES (?, ?, ?, ?);
        """, (
            config.user_id,
            "Card added",
            f"Added new {card_type} type card",
            datetime.datetime.now().strftime("%Y-%m-%d")
        ))

        # Commit the transaction
        conn.commit()

        print("Card added successfully and stored in History and Logs.")

    except sqlite3.Error as e:
        print("Database error:", e)
        conn.rollback()  # Roll back changes if an error occurs


def deleteCard(conn):
    try:
        cursor = conn.cursor()

        # Gather card details
        card_number = input("Enter card number (16 digits no spaces): ").strip()

        # Delete the card from the database
        cursor.execute("""
            DELETE FROM cards
            WHERE card_number = ? 
            AND user_id = ?;
        """, (card_number, config.user_id))

        # Commit the transaction
        conn.commit()

        # Add into history table
        cursor.execute("""
        INSERT INTO history (user_id, action_type, action_details, action_timestamp)
        VALUES (?, ?, ?, ?);
        """, (
            config.user_id,
            "Card deleted",
            f"Deleted card ************{card_number[-4:]} for {config.username}",
            datetime.datetime.now().strftime("%Y-%m-%d")
        ))

        # Commit the transaction
        conn.commit()

        print("\nCard deleted successfully and stored in History and Logs.")

    except sqlite3.Error as e:
        print("Database error:", e)
        conn.rollback()  # Roll back changes if an error occurs

def updateCard(conn):
    try:
        cursor = conn.cursor()

        print("Select a card to update:")
        retrieveCard(conn)

        # Gather card details
        card_number = input("Enter card number (16 digits no spaces): ").strip()

        # Check if the card number exists and is 16 digits
        cursor.execute("SELECT card_number FROM cards WHERE card_number = ?", (card_number,))
        existing_card = cursor.fetchone()

        if not existing_card:
            print("\nCard number does not exist. Please try again.")
            return 

        if not card_number.isdigit() or len(card_number) != 16:
            print("\nInvalid card number. Please try again.")
            return

        cardholder_name = input("Enter cardholder name: ").strip()
        card_type = input("Enter card type ('Visa', 'MasterCard', 'American Express' Only): ").strip()
        expiration_date = input("Enter expiration date (YYYY-MM): ").strip()
        billing_address = input("Enter billing address: ").strip()

        # Validate card type
        if card_type not in ['Visa', 'MasterCard', 'American Express']:
            print("Invalid card type. Please try again.")
            return

        # Update the card in the database
        cursor.execute("""
            UPDATE cards
            SET cardholder_name = ?, card_type = ?, expiration_date = ?, billing_address = ?
            WHERE card_number = ? AND user_id = ?;
        """, (cardholder_name, card_type, expiration_date, billing_address, card_number, config.user_id))

        # Commit the transaction
        conn.commit()

        # Add into history table
        cursor.execute("""
        INSERT INTO history (user_id, action_type, action_details, action_timestamp)
        VALUES (?, ?, ?, ?);
        """, (
            config.user_id,
            "Card updated",
            f"Updated card ************{card_number[-4:]} for {config.username}",
            datetime.datetime.now().strftime("%Y-%m-%d")
        ))

        # Commit the transaction
        conn.commit()

        print("Card updated successfully and stored in History and Logs.")

    except sqlite3.Error as e:
        print("Database error:", e)
        conn.rollback()  # Roll back changes if an error occurs