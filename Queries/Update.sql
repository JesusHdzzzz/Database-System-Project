-- Update password for a User
UPDATE Passwords
SET password_plain = 'newpassword456'
WHERE user_id = 2 AND password_plain = 'mypassword456';

-- Update User's email
UPDATE Users
SET email = 'alice_w_new@example.com'
WHERE username = 'alice_w';

-- Update card expiration date for a specific card
UPDATE CreditDebitCards
SET expiration_date = '2028-05'
WHERE card_number = '4111111111111111';

-- Update device information for a user
UPDATE DevicesLocations
SET device_name = 'Alice’s iPad', device_type = 'Tablet'
WHERE user_id = 1 AND device_name = "Alice's iPhone";

-- Update group domain name
UPDATE Groups
SET group_domain = 'updatedcompanya.com'
WHERE group_name = 'Company A';
