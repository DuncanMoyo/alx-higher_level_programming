#!/usr/bin/python3

"""
Lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
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
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    # Prints the results in the format specified in the prompt
    for row in cur.fetchall():
        print(row)
    # Closes the cursor and database connection
    cur.close()
    db.close()
