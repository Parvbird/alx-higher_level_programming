-- The script that creates a table second_table in the database hbtn_0c_0
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
);

INSERT INTO second_table (id, name, score)
VALUES
	(1, "Jane", 10),
	(2, "Tom", 3),
	(3, "Joshua", 14),
	(4, "Kelvin", 8);
