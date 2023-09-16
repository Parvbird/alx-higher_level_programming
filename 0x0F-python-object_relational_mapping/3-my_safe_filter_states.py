#!/usr/bin/python3
""" Script that takes an argument and displays all values
    in the states table where the name matches with the argument
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    user_name, password, database, match = argv[1], argv[2], argv[3], argv[4]

    # This establish the connection to the database through the MySQLdb module
    db = MySQLdb.connect(
        host="localhost",
        user=user_name,
        passwd=password,
        db=database,
        port=3306
    )

    # This create the working environment using the cursor object
    cursor_object = db.cursor()

    query = """
    SELECT * from states
    WHERE name = %s
    ORDER BY states.id ASC
    """

    cursor_object.execute(query, (match,))
    rows = cursor_object.fetchall()
    for row in rows:
        print("{}".format(row))

    cursor_object.close()
    db.close()
