-- Correct Users table
CREATE TABLE Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Passwords table without encryption
CREATE TABLE Passwords (
    password_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INT,
    password_plain TEXT NOT NULL, -- Storing plain password is insecure
    website_id INT, 
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (website_id) REFERENCES Websites(website_id)
);


-- Websites table (unchanged)
CREATE TABLE Websites (
    website_id INTEGER PRIMARY KEY AUTOINCREMENT,
    website_name TEXT NOT NULL,
    website_url TEXT NOT NULL
);

-- CreditDebitCards table without encryption
CREATE TABLE CreditDebitCards (
    card_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INT,
    cardholder_name TEXT NOT NULL,
    card_number TEXT NOT NULL, -- Storing plain card number
    card_type TEXT NOT NULL CHECK (card_type IN ('Visa', 'MasterCard', 'American Express')),
    expiration_date TEXT NOT NULL,
    cvv TEXT NOT NULL,
    billing_address TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES Users(user_id)
);

-- History table (unchanged)
CREATE TABLE History (
    history_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INT,
    action_type TEXT NOT NULL, -- "Password change, card added, etc"
    action_details TEXT, -- Additional details
    action_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES Users(user_id)
);

-- DevicesLocations table (unchanged)
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
    FOREIGN KEY(user_id) REFERENCES Users(user_id)
);

CREATE TABLE Groups (
    group_id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_name TEXT NOT NULL,
    group_domain TEXT NOT NULL,
    group_type TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Group_Users (
    group_id INTEGER,
    user_id INTEGER,
    email TEXT NOT NULL,
    PRIMARY KEY (group_id, user_id),
    FOREIGN KEY (group_id) REFERENCES Groups(group_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE Group_Passwords (
    group_id INTEGER,
    password_id INTEGER,
    PRIMARY KEY (group_id, password_id),
    FOREIGN KEY (group_id) REFERENCES Groups(group_id),
    FOREIGN KEY (password_id) REFERENCES Passwords(password_id)
);

CREATE TABLE User_Websites (
    user_id INT,
    website_id INT,
    PRIMARY KEY (user_id, website_id),  -- Composite primary key to ensure uniqueness
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (website_id) REFERENCES Websites(website_id)
);
