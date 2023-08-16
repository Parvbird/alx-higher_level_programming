-- The script would lists all cities contained in a database

SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states on cities.state_id = states.id
ORDER BY id;
