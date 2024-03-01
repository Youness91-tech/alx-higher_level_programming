#!/usr/bin/python3
""" lists all State objects that
contain the letter a from the database hbtn_0e_6_usa """
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter_by(name=sys.argv[4]).first()
    if state is not None:
        print(str(state.id))
    else:
        print("Not found")
    session.close()
