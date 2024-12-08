-- Retrieve the password for a specific user and website
SELECT web_pass
FROM web_pass, web, users
WHERE web_pass.user_id = users.user_id
AND web_pass.website_id = web.website_id
AND users.user_id = 13
AND web.website_id = 19;

-- Retrieve all passwords for a specific user
SELECT web_pass.web_pass
FROM web_pass, web, users
WHERE web_pass.user_id = users.user_id
AND web_pass.website_id = web.website_id
AND users.user_id = 13;

-- Retrieve the password for a specific user and group 
SELECT group_email_pass
FROM group_pass, groups, users
WHERE group_pass.user_id = users.user_id
AND group_pass.group_id = groups.group_id
AND users.user_id = 13
AND groups.group_id = 5;

-- Create a new password for a website
INSERT INTO web_pass (user_id, website_id, web_pass)
VALUES (13, 19, 'newpassword'); 
