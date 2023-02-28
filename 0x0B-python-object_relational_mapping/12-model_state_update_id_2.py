#!/usr/bin/python3
"""
Changes the name of a State object with id = 2 to "New Mexico"
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    # Set up the connection to the database
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create the engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, db_name), pool_pre_ping=True)

    # Create the session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database for the state with id=2
    state = session.query(State).filter_by(id=2).first()

    if state is None:
        print("Not found")
    else:
        # Update the state name
        state.name = "New Mexico"
        # Commit the changes
        session.commit()

        # Print the updated state id
        print(state.id)

    # Close the session
    session.close()
