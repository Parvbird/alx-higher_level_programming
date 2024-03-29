#!/usr/bin/python3
"""
Script lists all State objects from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

username, password, db_name = argv[1], argv[2], argv[3]

if __name__ == "__main__":
    # create engine
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}'
        )
    Base.metadata.create_all(engine)

    # This binds the sessions to engine to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()  # this creates a session

    # This queries the state objects
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    # close(end)
    session.close()
