--------------------------DELETE---------------------------

-- Delete a User by username
DELETE FROM users
WHERE username = 'bob_d';

-- Delete a User's password record
DELETE FROM pass
WHERE user_id = 3 AND m_pass = 'admin789';

-- Remove a Group
DELETE FROM groups
WHERE group_name = 'Club D';

-- Delete a specific credit card entry
DELETE FROM cards
WHERE card_number = '6111111111111111';

-- Remove a device location entry for a user
DELETE FROM devloc
WHERE user_id = 2 AND device_name = "Bob's Laptop";


--------------------------INSERT---------------------------

-- Add a new user
INSERT INTO users (username, email) VALUES ('john_s', 'john_s@example.com');

-- Add a new website
INSERT INTO web (website_name, website_url) VALUES ('StackOverflow', 'https://stackoverflow.com');

-- Add a Credit card for an Existing User
INSERT INTO cards (user_id, cardholder_name, card_number, card_type, expiration_date, cvv, billing_address)
VALUES (1, 'Alice W', '4111222233334444', 'Visa', '2027-01', '123', '123 Elm St, Springfield');

-- Add a new entry in DeviceLocations table
INSERT INTO devloc (user_id, device_name, device_type, operating_system, ip_address, city, country)
VALUES (3, "Carla's New Tablet", 'Tablet', 'Android', "192.168.1.100", 'Springfield', 'USA');

-- Add a New History Action for a User
INSERT INTO history (user_id, action_type, action_details)
VALUES (2, 'Password change', 'Updated LinkedIn password');


--------------------------SELECT---------------------------

-- Retrieve all users
SELECT * FROM users;

-- Get all Credit Card Information for a specific user
SELECT * FROM cards WHERE user_id = 1;

-- Get all websites and their URLs
SELECT website_name, website_url FROM web;

-- Find Users with password changes logged in history 
SELECT user_id, action_type, action_timestamp FROM history WHERE action_type = 'Password change';

-- Retrieve Login Device information for a specific user
SELECT device_name, device_type, operating_system, ip_address FROM devloc WHERE user_id = 3;

-------------------------UPDATE----------------------------

-- Update password for a User
UPDATE pass
SET m_pass = 'newpassword456'
WHERE user_id = 2 AND m_pass = 'mypassword456';

-- Update User's email
UPDATE users
SET email = 'alice_w_new@example.com'
WHERE username = 'alice_w';

-- Update card expiration date for a specific card
UPDATE cards
SET expiration_date = '2028-05'
WHERE card_number = '4111111111111111';

-- Update device information for a user
UPDATE devloc
SET device_name = 'Alice’s iPad', device_type = 'Tablet'
WHERE user_id = 1 AND device_name = "Alice's iPhone";

-- Update group domain name
UPDATE groups
SET group_domain = 'updatedcompanya.com'
WHERE group_name = 'Company A';

-------------------------EXTRAS----------------------------

-- Add a new user to an existing group
INSERT INTO group_u (group_id, user_id, email) VALUES (2, 1, 'alice_w@companyb.com');

-- Assign an existing password to a new group
INSERT INTO group_link (group_id, password_id) VALUES (1, 5);

-- Retrieve all groups a user belongs to
SELECT g.group_name, g.group_domain
FROM groups g
JOIN group_u gu ON g.group_id = gu.group_id
WHERE gu.user_id = 1;

-- Find all passwords for a specific group
SELECT pass.m_pass
FROM pass
JOIN group_link gl ON pass.password_id = gl.password_id
WHERE gl.group_id = 3;

-- Retrieve all users and their devices with login locations
SELECT u.username, d.device_name, d.device_type, d.city, d.country
FROM users u
JOIN devloc d ON u.user_id = d.user_id;

-- Add a new password for a user
INSERT INTO pass (user_id, m_pass) VALUES (1, 'securepassword987');

-- Link a user to a new website
INSERT INTO user_web (user_id, website_id) VALUES (1, 3);

-- Retrieve all websites linked to a user
SELECT w.website_name, w.website_url
FROM web w
JOIN user_web uw ON w.website_id = uw.website_id
WHERE uw.user_id = 1;

-- Count all password changes in history
SELECT COUNT(*) AS password_changes
FROM history
WHERE action_type = 'Password change';

-- Add a new group for an institution and link users
INSERT INTO groups (group_name, group_domain, group_type) VALUES ('New Institution', 'newinstitution.edu', 'Educational');
INSERT INTO group_u (group_id, user_id, email) VALUES (11, 4, 'daniel_t@newinstitution.edu');

-- Retrieves username, group details, and password IDs linked to the group
SELECT users.username, groups.group_id, groups.group_name, group_link.password_id
FROM users
JOIN group_u ON users.user_id = group_u.user_id
JOIN groups ON groups.group_id = group_u.group_id
JOIN group_link ON groups.group_id = group_link.group_id;

-- Retrieves username and website details
SELECT users.username, web.website_id, web.website_name
FROM users
JOIN user_web ON users.user_id = user_web.user_id
JOIN web ON web.website_id = user_web.website_id;
