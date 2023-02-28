#!/usr/bin/python3
"""
prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":

    # Connecting to the database
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}"
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)

    # Creating a Session class
    Session = sessionmaker(bind=engine)

    # Creating a Session
    session = Session()

    # Querying for the state object
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    if state is not None:
        # Displaying the state's id
        print("{}".format(state.id))
    else:
        print("Not found")

    # Closing the session
    session.close()
