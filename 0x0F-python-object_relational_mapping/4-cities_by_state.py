#!/usr/bin/python3
"""Return all rows from cities"""
from MySQLdb import connect
from sys import argv


if __name__ == "__main__":
    db = connect(host="localhost", user=argv[1], passwd=argv[2],
                 db=argv[3], port=3306)

    cr = db.cursor()

    cr.execute("SELECT cities.id, cities.name, states.name FROM cities\
               INNER JOIN states ON states.id=cities.state_id\
               ORDER BY cities.id ASC")

    rows = cr.fetchall()
    for row in rows:
        print(row)

    cr.close()
    db.close()
