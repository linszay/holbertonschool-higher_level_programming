#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":

    # Connecting to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Creating a cursor object
    cursor = db.cursor()

    # Executing the query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Retrieving the results
    results = cursor.fetchall()

    # Displaying the results
    for state in results:
        if state[0] <= 5:
            print(state)

    # Closing the connection to the database
    db.close()
