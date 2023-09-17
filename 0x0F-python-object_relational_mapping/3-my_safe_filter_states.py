#!/usr/bin/python3
"""Filter out the content of the selected rows"""
from MySQLdb import connect
from sys import argv


if __name__ == "__main__":
    db = connect(host="localhost", user=argv[1], passwd=argv[2],
                 db=argv[3])

    cr = db.cursor()

    cr.execute(f"SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC", (argv[4],))

    states_data = cr.fetchall()
    for row in states_data:
        print(row)

    cr.close()
    db.close()
