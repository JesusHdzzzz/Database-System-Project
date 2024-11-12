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
