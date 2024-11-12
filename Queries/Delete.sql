-- Delete a User by username
DELETE FROM Users
WHERE username = 'bob_d';

-- Delete a User's password record
DELETE FROM Passwords
WHERE user_id = 3 AND password_plain = 'admin789';

-- Remove a Group
DELETE FROM Groups
WHERE group_name = 'Club D';

-- Delete a specific credit card entry
DELETE FROM CreditDebitCards
WHERE card_number = '6111111111111111';

-- Remove a device location entry for a user
DELETE FROM DevicesLocations
WHERE user_id = 2 AND device_name = "Bob's Laptop";
