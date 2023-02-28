#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connecting to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Creating a cursor object
    cursor = db.cursor()

    # Executing the query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Retrieving the results
    results = cursor.fetchall()

    # Displaying the results
    for row in results:
        print(row)

    # Closing the connection
    db.close()
