CREATE TABLE Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL, -- Store encrypted password
    email TEXT NOT NULL UNIQUE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP);

CREATE TABLE Passwords (
    password_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INT,
    website_id INT,
    password_encrypted TEXT NOT NULL, -- Store encrypted password
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES Users(user_id),
    FOREIGN KEY(website_id) REFERENCES Websites(website_id));

CREATE TABLE Websites (
    website_id INTEGER PRIMARY KEY AUTOINCREMENT,
    website_name TEXT NOT NULL,
    website_url TEXT NOT NULL);

CREATE TABLE CreditDebitCards (
    card_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INT,
    cardholder_name TEXT NOT NULL,
    card_number_encrypted TEXT NOT NULL, -- Store encrypted card number
    card_type TEXT NOT NULL, -- Visa, Mastercard, etc
    expiration_date TEXT NOT NULL,
    cvv_encrypted TEXT NOT NULL,
    billing_address TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES Users(user_id));

CREATE TABLE History (
    history_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INT,
    action_type TEXT NOT NULL, -- "Password change, card added, etc"
    action_details TEXT -- Additional details
    action_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES Users(user_id));

CREATE TABLE DevicesLocations (
    entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INT,
    device_name TEXT, -- Alex's iphone
    device_type TEXT, -- Mobile, PC, Laptop
    operating_system TEXT, -- iOS, Windows, Linux
    ip_address TEXT, 
    city TEXT,
    country TEXT,
    login_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES Users(user_id));