INSERT INTO Users (username, email) VALUES
('alexsmith', 'alexsmith@example.com'),
('john_doe', 'john.doe@example.com'),
('jane_doe', 'jane.doe@example.com'),
('michael_j', 'michael.j@example.com'),
('sarah_connor', 'sarah.connor@example.com'),
('tom_clark', 'tom.clark@example.com'),
('emma_watson', 'emma.watson@example.com'),
('chris_lee', 'chris.lee@example.com'),
('lisa_adams', 'lisa.adams@example.com'),
('david_brown', 'david.brown@example.com');

INSERT INTO Websites (website_name, website_url) VALUES
('Google', 'https://www.google.com'),
('Facebook', 'https://www.facebook.com'),
('Twitter', 'https://www.twitter.com'),
('LinkedIn', 'https://www.linkedin.com'),
('GitHub', 'https://www.github.com'),
('Amazon', 'https://www.amazon.com'),
('YouTube', 'https://www.youtube.com'),
('Instagram', 'https://www.instagram.com'),
('Reddit', 'https://www.reddit.com'),
('Netflix', 'https://www.netflix.com');

INSERT INTO Passwords (user_id, password_plain, website_id) VALUES
(1, 'Password123!', 1),
(2, 'SecurePass456', 2),
(3, 'Admin789!', 3),
(4, 'ConnorRules111', 4),
(5, 'Qwerty2024!', 5),
(6, 'ZxcvbStrong333', 6),
(7, 'EmmaSecret444', 7),
(8, 'ChrisPass555', 8),
(9, 'LisaHidden666', 9),
(10, 'DavidFinal777', 10);

INSERT INTO CreditDebitCards (user_id, cardholder_name, card_number, card_type, expiration_date, cvv, billing_address) VALUES
(1, 'Alex Smith', '4111111111111111', 'Visa', '12/25', '123', '123 Main St, Anytown, USA'),
(2, 'John Doe', '5500000000000004', 'MasterCard', '11/26', '456', '456 Elm St, Othertown, USA'),
(3, 'Jane Doe', '340000000000009', 'American Express', '10/27', '789', '789 Pine St, Anothertown, USA'),
(4, 'Michael J', '4111111111112222', 'Visa', '01/28', '321', '101 Oak St, Newtown, USA'),
(5, 'Sarah Connor', '5500000000003333', 'MasterCard', '02/29', '654', '202 Maple St, Oldtown, USA'),
(6, 'Tom Clark', '340000000000444', 'American Express', '03/30', '987', '303 Cherry St, Smalltown, USA'),
(7, 'Emma Watson', '4111111111115555', 'Visa', '04/31', '231', '404 Cedar St, Bigcity, USA'),
(8, 'Chris Lee', '5500000000006666', 'MasterCard', '05/32', '564', '505 Birch St, Littletown, USA'),
(9, 'Lisa Adams', '340000000000777', 'American Express', '06/33', '897', '606 Walnut St, Middletown, USA'),
(10, 'David Brown', '4111111111118888', 'Visa', '07/34', '345', '707 Spruce St, Uptown, USA');

INSERT INTO History (user_id, action_type, action_details) VALUES
(1, 'Password Change', 'Updated Google password'),
(2, 'Card Added', 'Added MasterCard ending in 0004'),
(3, 'Login', 'Logged in from a new device'),
(4, 'Password Reset', 'Reset LinkedIn password'),
(5, 'Card Updated', 'Updated expiration date for Visa'),
(6, 'Password Change', 'Changed password for Amazon'),
(7, 'Card Removed', 'Removed old Visa card'),
(8, 'Login Attempt', 'Attempted login from unknown location'),
(9, 'Password Reset', 'Reset GitHub password'),
(10, 'Profile Update', 'Updated email address');

INSERT INTO DevicesLocations (user_id, device_name, device_type, operating_system, ip_address, city, country) VALUES
(1, 'Alex’s iPhone', 'Mobile', 'iOS', '192.168.1.2', 'San Francisco', 'USA'),
(2, 'John’s Laptop', 'Laptop', 'Windows', '192.168.1.3', 'New York', 'USA'),
(3, 'Jane’s Tablet', 'Tablet', 'Android', '192.168.1.4', 'Chicago', 'USA'),
(4, 'Michael’s PC', 'PC', 'Linux', '192.168.1.5', 'Los Angeles', 'USA'),
(5, 'Sarah’s iPad', 'Tablet', 'iOS', '192.168.1.6', 'Seattle', 'USA'),
(6, 'Tom’s MacBook', 'Laptop', 'macOS', '192.168.1.7', 'Boston', 'USA'),
(7, 'Emma’s Surface', 'Tablet', 'Windows', '192.168.1.8', 'Austin', 'USA'),
(8, 'Chris’s Phone', 'Mobile', 'Android', '192.168.1.9', 'Denver', 'USA'),
(9, 'Lisa’s PC', 'PC', 'Windows', '192.168.1.10', 'Miami', 'USA'),
(10, 'David’s Chromebook', 'Laptop', 'ChromeOS', '192.168.1.11', 'Phoenix', 'USA');

INSERT INTO Groups (group_name, group_domain, group_type) VALUES
('Dev Team', 'Engineering', 'Work'),
('QA Team', 'Engineering', 'Work'),
('Family', 'Personal', 'Social'),
('Friends', 'Personal', 'Social'),
('Fitness Club', 'Hobby', 'Recreation'),
('Book Club', 'Hobby', 'Recreation'),
('Study Group', 'Education', 'Academic'),
('Volunteer Group', 'Community', 'Social'),
('Gamer Guild', 'Gaming', 'Recreation'),
('Travel Buddies', 'Personal', 'Recreation');

INSERT INTO Group_Users (group_id, user_id, email) VALUES
(1, 1, 'alexsmith@example.com'),
(1, 2, 'john.doe@example.com'),
(2, 3, 'jane.doe@example.com'),
(3, 4, 'michael.j@example.com'),
(4, 5, 'sarah.connor@example.com'),
(5, 6, 'tom.clark@example.com'),
(6, 7, 'emma.watson@example.com'),
(7, 8, 'chris.lee@example.com'),
(8, 9, 'lisa.adams@example.com'),
(9, 10, 'david.brown@example.com');

INSERT INTO Group_Passwords (group_id, password_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10);

INSERT INTO User_Websites (user_id, website_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10);
