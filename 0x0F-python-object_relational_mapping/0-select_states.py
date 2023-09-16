#!/usr/bin/python3
""" Script that lists all states from a database """

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    user_name, password, database = argv[1], argv[2], argv[3]

    # This makes a connection to the database through the MySQLdb module
    db = MySQLdb.connect(
        host="localhost",
        user=user_name,
        passwd=password,
        db=database,
        port=3306
    )

    # This creates a working environment using cursor object
    # to perform operations on the database
    cursor_object = db.cursor()

    cursor_object.execute("SELECT * from states ORDER BY id ASC")
    rows = cursor_object.fetchall()
    for row in rows:
        print("{}".format(row))

    cursor_object.close()
    db.close()
