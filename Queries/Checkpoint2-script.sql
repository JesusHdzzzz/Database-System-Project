--------------------------DELETE---------------------------

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

--------------------------INSERT---------------------------

-- Add a new user
INSERT INTO Users (username, email) VALUES ('john_s', 'john_s@example.com');

-- Add a new website
INSERT INTO Websites (website_name, website_url) VALUES ('StackOverflow', 'https://stackoverflow.com');

-- Add a Credit card for an Existing User
INSERT INTO CreditDebitCards (user_id, cardholder_name, card_number, card_type, expiration_date, cvv, billing_address)
VALUES (1, 'Alice W', '4111222233334444', 'Visa', '2027-01', '123', '123 Elm St, Springfield');

-- Add a new entry in DeviceLocations table
INSERT INTO DevicesLocations (user_id, device_name, device_type, operating_system, ip_address, city, country)
VALUES (3, "Carla's New Tablet", 'Tablet', 'Android', "192.168.1.100", 'Springfield', 'USA');

-- Add a New History Action for a User
INSERT INTO History (user_id, action_type, action_details)
VALUES (2, 'Password change', 'Updated LinkedIn password');

--------------------------SELECT---------------------------

-- Retrieve all users
SELECT * FROM Users;

-- Get all Credit Card Information for a specific user
SELECT * FROM CreditDebitCards WHERE user_id = 1;

-- Get all websites and their URLs
SELECT website_name, website_url FROM Websites;

-- Find Users with password changes logged in history 
SELECT user_id, action_type, action_timestamp FROM History WHERE action_type = 'Password change';

-- Retrieve Login Device information for a specific user
SELECT device_name, device_type, operating_system, ip_address FROM DevicesLocations WHERE user_id = 3;

-------------------------UPDATE----------------------------

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

-------------------------EXTRAS----------------------------

-- Add a new user to an existing group
INSERT INTO Group_Users (group_id, user_id, email) VALUES (2, 1, 'alice_w@companyb.com');

-- Assign an existing password to a new group
INSERT INTO Group_Passwords (group_id, password_id) VALUES (1, 5);

-- Retrieve all groups a user belongs to
SELECT g.group_name, g.group_domain
FROM Groups g
JOIN Group_Users gu ON g.group_id = gu.group_id
WHERE gu.user_id = 1;

-- Find all passwords for a specific group
SELECT p.password_plain
FROM Passwords p
JOIN Group_Passwords gp ON p.password_id = gp.password_id
WHERE gp.group_id = 3;

-- Retrieve all users and their devices with login locations
SELECT u.username, d.device_name, d.device_type, d.city, d.country
FROM Users u
JOIN DevicesLocations d ON u.user_id = d.user_id;

-- Add a new password for a user
INSERT INTO Passwords (user_id, password_plain) VALUES (1, 'securepassword987');

-- Link a user to a new website
INSERT INTO User_Websites (user_id, website_id) VALUES (1, 3);

-- Retrieve all websites linked to a user
SELECT w.website_name, w.website_url
FROM Websites w
JOIN User_Websites uw ON w.website_id = uw.website_id
WHERE uw.user_id = 1;

-- Count all password changes in history
SELECT COUNT(*) AS password_changes
FROM History
WHERE action_type = 'Password change';

-- Add a new group for an institution and link users
INSERT INTO Groups (group_name, group_domain, group_type) VALUES ('New Institution', 'newinstitution.edu', 'Educational');
INSERT INTO Group_Users (group_id, user_id, email) VALUES (11, 4, 'daniel_t@newinstitution.edu');
