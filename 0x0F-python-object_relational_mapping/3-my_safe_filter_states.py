#!/usr/bin/python3

"""
takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
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

    # Executes the SQL query to retrieve all states starting with N
    cur = db.cursor()
    arg = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s", (arg,))

    # Prints the results in the format specified in the prompt
    for row in cur.fetchall():
        print(row)

    # Closes the cursor and database connection
    cur.close()
    db.close()
