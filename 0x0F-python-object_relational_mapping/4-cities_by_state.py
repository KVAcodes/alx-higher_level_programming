#!/usr/bin/python3
"""This script lists all the states from the database hbtn_0e_0_usa.
with a name starting with N (upper N).
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities "
                "JOIN states ON cities.state_id=states.id ORDER BY cities.id;")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
