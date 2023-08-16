-- The script would creates a database and a user

-- This would create a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- This would create a user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- This would grant user privilege
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
