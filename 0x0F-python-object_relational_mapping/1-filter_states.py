#!/usr/bin/python3
""" lists all states with a name starting with
N (upper N) from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    connc = MySQLdb.connect(host="localhost", user=sys.argv[1],
                            passwd=sys.argv[2], port=3306, db=sys.argv[3])
    cur = connc.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY\
            'N%' ORDER BY id ASC")
    row = cur.fetchall()
    for state in row:
        print(state)
    cur.close()
    connc.close()
