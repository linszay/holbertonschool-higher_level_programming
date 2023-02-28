#!/usr/bin/python3
"""
takes in arguments and displays all values in the
states table of hbtn_0e_0_usa where name matches the
argument. But this time, write one that is safe from
MySQL injections!
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

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

    # Creating the query
    query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"

    # Executing the query
    cursor.execute(query, (state_name,))

    # Retrieving the results
    results = cursor.fetchall()

    # Displaying the results
    for state in results:
        print(state)

    # Closing the connection to the database
    db.close()
