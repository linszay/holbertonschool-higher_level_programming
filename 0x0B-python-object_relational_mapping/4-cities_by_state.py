#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
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
    cursor.execute("SELECT cities.id, cities.name, states.name\
                   FROM cities JOIN states\
                   WHERE cities.state_id = states.id\
                   ORDER BY cities.id ASC")

    # Retrieving the results
    results = cursor.fetchall()

    # Displaying the results
    for cities in results:
        print(cities)

    # Closing the connection to the database
    db.close()
