#!/usr/bin/python3
"""
lists all State objects that contain the letter a
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Creating the engine that connects to the database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Creating a Session class
    Session = sessionmaker(bind=engine)

    # Creating a session
    session = Session()

    # Querying the database for states that contain the letter 'a'
    results = session.query(State).filter(
        State.name.like("%a%")).order_by(State.id)

    # Displaying the results
    for state in results:
        print("{}: {}".format(state.id, state.name))

    # Closing the session
    session.close()
