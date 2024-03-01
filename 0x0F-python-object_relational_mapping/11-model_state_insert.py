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
    session.add(State(name='Louisiana'))
    for state in session.query(State).filter(State.name == 'Louisiana'):
        print('{}'.format(state.id))
    session.commit()
