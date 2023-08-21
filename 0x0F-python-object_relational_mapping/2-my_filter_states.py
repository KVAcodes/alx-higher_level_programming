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
    cur.execute("SELECT * FROM states WHERE name = \"{}\" "
                "ORDER BY states.id;".format(sys.argv[4]))

    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
