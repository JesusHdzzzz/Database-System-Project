INSERT INTO Users (username, email, created_at) VALUES 
('alice_w', 'alice_w@example.com', '2024-01-01'),
('bob_d', 'bob_d@example.com', '2024-01-02'),
('carla_r', 'carla_r@example.com', '2024-01-03'),
('daniel_t', 'daniel_t@example.com', '2024-01-04'),
('eve_h', 'eve_h@example.com', '2024-01-05'),
('frank_j', 'frank_j@example.com', '2024-01-06'),
('grace_k', 'grace_k@example.com', '2024-01-07'),
('hank_l', 'hank_l@example.com', '2024-01-08'),
('ivy_m', 'ivy_m@example.com', '2024-01-09'),
('jack_o', 'jack_o@example.com', '2024-01-10');

INSERT INTO Websites (website_name, website_url) VALUES 
('Google', 'https://www.google.com'),
('Facebook', 'https://www.facebook.com'),
('Amazon', 'https://www.amazon.com'),
('Twitter', 'https://www.twitter.com'),
('LinkedIn', 'https://www.linkedin.com'),
('YouTube', 'https://www.youtube.com'),
('Instagram', 'https://www.instagram.com'),
('Reddit', 'https://www.reddit.com'),
('GitHub', 'https://www.github.com'),
('Netflix', 'https://www.netflix.com');

INSERT INTO CreditDebitCards (user_id, cardholder_name, card_number, card_type, expiration_date, cvv, billing_address, created_at) VALUES 
(1, 'Alice W', '4111111111111111', 'Visa', '2025-05', '123', '123 Elm St, Springfield', '2024-01-11'),
(2, 'Bob D', '5111111111111111', 'MasterCard', '2026-04', '456', '456 Oak St, Springfield', '2024-01-12'),
(3, 'Carla R', '6111111111111111', 'American Express', '2025-03', '789', '789 Maple St, Springfield', '2024-01-13'),
(4, 'Daniel T', '4111111111112222', 'Visa', '2026-06', '321', '321 Pine St, Springfield', '2024-01-14'),
(5, 'Eve H', '5111111111112222', 'MasterCard', '2025-07', '654', '654 Cedar St, Springfield', '2024-01-15'),
(6, 'Frank J', '6111111111112222', 'American Express', '2025-08', '987', '987 Birch St, Springfield', '2024-01-16'),
(7, 'Grace K', '4111111111113333', 'Visa', '2026-09', '432', '432 Walnut St, Springfield', '2024-01-17'),
(8, 'Hank L', '5111111111113333', 'MasterCard', '2025-10', '765', '765 Chestnut St, Springfield', '2024-01-18'),
(9, 'Ivy M', '6111111111113333', 'American Express', '2026-11', '098', '098 Cypress St, Springfield', '2024-01-19'),
(10, 'Jack O', '4111111111114444', 'Visa', '2026-12', '210', '210 Beech St, Springfield', '2024-01-20');

INSERT INTO History (user_id, action_type, action_details, action_timestamp) VALUES 
(1, 'Password change', 'Updated Google password', '2024-01-21'),
(2, 'Card added', 'Added new Visa card', '2024-01-22'),
(3, 'Password change', 'Updated Facebook password', '2024-01-23'),
(4, 'Login', 'Logged in from new device', '2024-01-24'),
(5, 'Password reset', 'Reset LinkedIn password', '2024-01-25'),
(6, 'Card added', 'Added new MasterCard', '2024-01-26'),
(7, 'Password change', 'Updated Instagram password', '2024-01-27'),
(8, 'Login', 'Logged in from new device', '2024-01-28'),
(9, 'Password change', 'Updated GitHub password', '2024-01-29'),
(10, 'Password reset', 'Reset Amazon password', '2024-01-30');

INSERT INTO DevicesLocations (user_id, device_name, device_type, operating_system, ip_address, city, country, login_timestamp) VALUES 
(1, "Alice\'s iPhone", 'Mobile', 'iOS', '192.168.1.2', 'Springfield', 'USA', '2024-01-31'),
(2, "Bob\'s Laptop", 'PC', 'Windows', '192.168.1.3', 'Springfield', 'USA', '2024-01-32'),
(3, "Carla\'s Tablet", 'Mobile', 'Android', '192.168.1.4', 'Springfield', 'USA', '2024-01-33'),
(4, "Daniel\'s Desktop", 'PC', 'Linux', '192.168.1.5', 'Springfield', 'USA', '2024-01-34'),
(5, "Eve\'s iPad", 'Mobile', 'iOS', '192.168.1.6', 'Springfield', 'USA', '2024-01-35'),
(6, "Frank\'s Phone", 'Mobile', 'Android', '192.168.1.7', 'Springfield', 'USA', '2024-01-36'),
(7, "Grace\'s Laptop", 'PC', 'Windows', '192.168.1.8', 'Springfield', 'USA', '2024-01-37'),
(8, "Hank\'s iPhone", 'Mobile', 'iOS', '192.168.1.9', 'Springfield', 'USA', '2024-01-38'),
(9, "Ivy\'s Tablet", 'Mobile', 'Android', '192.168.1.10', 'Springfield', 'USA', '2024-01-39'),
(10, "Jack\'s Desktop", 'PC', 'Linux', '192.168.1.11', 'Springfield', 'USA', '2024-01-40');

INSERT INTO Groups (group_name, group_domain, group_type, created_at) VALUES 
('Company A', 'companya.com', 'Enterprise', '2024-01-01'),
('Company B', 'companyb.com', 'Enterprise', '2024-01-02'),
('School C', 'schoolc.edu', 'Educational', '2024-01-03'),
('Club D', 'clubd.org', 'Nonprofit', '2024-01-04'),
('Research Lab E', 'researche.org', 'Research', '2024-01-05'),
('Startup F', 'startupf.io', 'Enterprise', '2024-01-06'),
('University G', 'universityg.edu', 'Educational', '2024-01-07'),
('Group H', 'grouph.com', 'Community', '2024-01-08'),
('Foundation I', 'foundationi.org', 'Nonprofit', '2024-01-09'),
('Collective J', 'collectivej.com', 'Community', '2024-01-10');


INSERT INTO Group_Users (group_id, user_id, email) VALUES 
(1, 1, 'alice_w@companya.com'),
(2, 2, 'bob_d@companyb.com'),
(3, 3, 'carla_r@schoolc.edu'),
(4, 4, 'daniel_t@clubd.org'),
(5, 5, 'eve_h@researche.org'),
(6, 6, 'frank_j@startupf.io'),
(7, 7, 'grace_k@universityg.edu'),
(8, 8, 'hank_l@grouph.com'),
(9, 9, 'ivy_m@foundationi.org'),
(10, 10, 'jack_o@collectivej.com');


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

INSERT INTO Passwords (user_id, password_plain, created_at) VALUES 
(1, 'password123', '2024-01-11'),
(2, 'mypassword456', '2024-01-12'),
(3, 'admin789', '2024-01-13'),
(4, 'secretkey111', '2024-01-14'),
(5, 'qwerty222', '2024-01-15'),
(6, 'zxcvb333', '2024-01-16'),
(7, 'lmnop444', '2024-01-17'),
(8, 'asdfg555', '2024-01-18'),
(9, 'hjkl666', '2024-01-19'),
(10, 'yuiop777', '2024-01-20');

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
