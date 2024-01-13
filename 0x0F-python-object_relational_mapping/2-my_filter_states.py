#!/usr/bin/python3
""" takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument """
import MySQLdb
import sys


if __name__ == "__main__":
    connc = MySQLdb.connect(host="localhost", user=sys.argv[1],
                            passwd=sys.argv[2], port=3306, db=sys.argv[3])
    cur = connc.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY\
        '{}' ORDER BY id ASC".format(sys.argv[4]))
    row = cur.fetchall()
    for state in row:
        print(state)
    cur.close()
    connc.close()
