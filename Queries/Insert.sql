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
