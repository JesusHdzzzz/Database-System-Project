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
