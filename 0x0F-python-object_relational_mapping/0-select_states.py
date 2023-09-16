#!/usr/bin/python3
"""
Create a connect to mysql server by useing MySQLdb
and fetch some data from it
"""
from MySQLdb import connect
from sys import argv


if __name__ == "__main__":
    db = connect(host="localhost", user=argv[1], passwd=argv[2],
                 db=argv[3], port=3306)

    cr = db.cursor()

    data = cr.execute("""SELECT * FROM states ORDER BY id ASC""")
    fetched_data = data.fetchall()
    for row in fetched_data:
        print(row)
    cr.close()
    db.close()
