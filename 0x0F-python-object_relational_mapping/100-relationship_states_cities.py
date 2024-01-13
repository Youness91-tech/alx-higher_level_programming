#!/usr/bin/python3
""" creates the State “California” with
the City “San Francisco” from the database hbtn_0e_100_usa """
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add a new city with state
    my_state = State(name="California")
    my_city = City(name="San Francisco", state=my_state)
    session.add(my_state)
    session.add(my_city)
    session.commit()
