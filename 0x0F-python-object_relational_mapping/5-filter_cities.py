#!/usr/bin/python3

"""
takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connects to the MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306)

    # Executes the SQL query to retrieve all cities of the given state
    cur = db.cursor()
    cur.execute("SELECT * FROM cities WHERE state_id IN (SELECT id FROM states WHERE name=%s) ORDER BY id ASC", (sys.argv[4],))

    # Prints the results in the format specified in the prompt
    print(", ".join([row[2] for row in cur.fetchall()]))

    # Closes the cursor and database connection
    cur.close()
    db.close()
