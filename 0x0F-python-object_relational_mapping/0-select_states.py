#!/usr/bin/python3
"""
Create a connect to mysql server by useing MySQLdb
and fetch some data from it
"""
from MySQLdb import connect
import sys


if __name__ == "__main__":
    db = connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2],
                 db=sys.argv[3], port=3306)

    cr = db.cursor()

    cr.execute("""SELECT * FROM states ORDER BY id ASC""")
    fetched_data = cr.fetchall()
    for row in fetched_data:
        print(row)
    cr.close()
    db.close()
