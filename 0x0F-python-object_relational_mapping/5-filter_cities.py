#!/usr/bin/python3
"""Return all rows from cities"""
from MySQLdb import connect
from sys import argv


if __name__ == "__main__":
    db = connect(host="localhost", user=argv[1], passwd=argv[2],
                 db=argv[3], port=3306)

    cr = db.cursor()

    cr.execute("SELECT cities.name FROM cities\
               INNER JOIN states ON states.id=cities.state_id\
               WHERE states.name=%s ORDER BY cities.id ASC", (argv[4],))

    rows = cr.fetchall()
    for i, row in enumerate(rows):
        print(row[0], end="")
        if (i + 1 != len(rows)):
            print(", ", end="")
    print("")

    cr.close()
    db.close()
