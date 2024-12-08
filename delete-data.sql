-- Delete all records from Credit and Debit Cards table
DELETE FROM cards;
DELETE FROM sqlite_sequence WHERE name='cards';

-- Delete all records from Device Locations table
DELETE FROM devloc;
DELETE FROM sqlite_sequence WHERE name='devloc';

-- Delete all records from Group Pass table
DELETE FROM group_link;
DELETE FROM sqlite_sequence WHERE name='group_link';

-- Delete all records from Group Users table
DELETE FROM group_u;
DELETE FROM sqlite_sequence WHERE name='group_u';

-- Delete all records from Groups table
DELETE FROM groups;
DELETE FROM sqlite_sequence WHERE name='groups';

-- Delete all records from History table
DELETE FROM history;
DELETE FROM sqlite_sequence WHERE name='history';

-- Delete all records from Pass table (master passwords)
DELETE FROM pass;
DELETE FROM sqlite_sequence WHERE name='pass';

-- Delete all records from User Websites table
DELETE FROM user_web;
DELETE FROM sqlite_sequence WHERE name='user_web';

-- Delete all records from Users table
DELETE FROM users;
DELETE FROM sqlite_sequence WHERE name='users';

-- Delete all records from Websites table
DELETE FROM web;
DELETE FROM sqlite_sequence WHERE name='web';

-- Delete all records from Group Passwords table
DELETE FROM group_pass;
DELETE FROM sqlite_sequence WHERE name='group_pass';

-- Delete all records from Websites table
DELETE FROM web_pass;
DELETE FROM sqlite_sequence WHERE name='web_pass';