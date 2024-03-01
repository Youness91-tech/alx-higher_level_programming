#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    connc = MySQLdb.connect(host="localhost", user=sys.argv[1],
                            passwd=sys.argv[2], port=3306, db=sys.argv[3])
    cur = connc.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM\
        cities, states WHERE cities.state_id = states.id ")
    row = cur.fetchall()
    for state in row:
        print(state)
    cur.close()
    connc.close()
