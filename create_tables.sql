-- Users table (parent table)
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Passwords table
CREATE TABLE pass (
    password_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INT,
    m_pass TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES Users(user_id) ON DELETE CASCADE
);

-- Websites table
CREATE TABLE web (
    website_id INTEGER PRIMARY KEY AUTOINCREMENT,
    website_name TEXT NOT NULL,
    website_url TEXT NOT NULL
);

-- Web_passwords table
CREATE TABLE web_pass (
    user_id INT,
    website_id INT,
    web_pass TEXT NOT NULL,
    PRIMARY KEY (user_id, website_id),
    FOREIGN KEY(user_id) REFERENCES Users(user_id) ON DELETE CASCADE,
    FOREIGN KEY(website_id) REFERENCES Websites(website_id) ON DELETE CASCADE
);

-- CreditDebitCards table
CREATE TABLE cards (
    card_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INT,
    cardholder_name TEXT NOT NULL,
    card_number TEXT NOT NULL,
    card_type TEXT NOT NULL CHECK (card_type IN ('Visa', 'MasterCard', 'American Express')),
    expiration_date TEXT NOT NULL,
    cvv TEXT NOT NULL,
    billing_address TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES Users(user_id) ON DELETE CASCADE
);

-- History table
CREATE TABLE history (
    history_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INT,
    action_type TEXT NOT NULL, 
    action_details TEXT,
    action_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES Users(user_id) ON DELETE CASCADE
);

-- DevicesLocations table
CREATE TABLE devloc (
    entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INT,
    device_name TEXT,
    device_type TEXT,
    operating_system TEXT,
    ip_address TEXT,
    city TEXT,
    country TEXT,
    login_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES Users(user_id) ON DELETE CASCADE
);

-- Groups table
CREATE TABLE groups (
    group_id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_name TEXT NOT NULL,
    group_domain TEXT NOT NULL,
    group_type TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Group_Users table
CREATE TABLE group_u (
    group_id INTEGER,
    user_id INTEGER,
    email TEXT NOT NULL,
    PRIMARY KEY (group_id, user_id),
    FOREIGN KEY(group_id) REFERENCES Groups(group_id) ON DELETE CASCADE,
    FOREIGN KEY(user_id) REFERENCES Users(user_id) ON DELETE CASCADE
);

-- Group_Passwords table
CREATE TABLE group_link (
    group_id INTEGER,
    password_id INTEGER,
    PRIMARY KEY (group_id, password_id),
    FOREIGN KEY(group_id) REFERENCES Groups(group_id) ON DELETE CASCADE,
    FOREIGN KEY(password_id) REFERENCES Passwords(password_id) ON DELETE CASCADE
);

-- User_Websites table
CREATE TABLE user_web (
    user_id INT,
    website_id INT,
    PRIMARY KEY (user_id, website_id),
    FOREIGN KEY(user_id) REFERENCES Users(user_id) ON DELETE CASCADE,
    FOREIGN KEY(website_id) REFERENCES Websites(website_id) ON DELETE CASCADE
);

CREATE TABLE group_pass (
    group_id INTEGER, -- References the group the user belongs to
    user_id INTEGER, -- References the user within the group
    group_email_pass TEXT NOT NULL, -- Stores the password for the user's group email
    PRIMARY KEY (group_id, user_id), -- Composite primary key ensures unique group-user-password relationship
    FOREIGN KEY (group_id) REFERENCES groups(group_id) ON DELETE CASCADE, -- Cascade delete when a group is deleted
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Cascade delete when a user is deleted
);