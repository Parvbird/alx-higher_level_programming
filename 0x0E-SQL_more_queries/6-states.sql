-- The script would creates the database and table state
-- this creates a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- this creates a table
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL
);
