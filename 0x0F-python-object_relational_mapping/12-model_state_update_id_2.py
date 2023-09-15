#!/usr/bin/python3

"""
Changes the name of a State object from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    # Connects to the MySQL server running on localhost at port 3306
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Creates a session
    Session = sessionmaker(bind=engine)
    session = Session()

     # Queries the database to retrieve the state with id = 2 and changes its name to New Mexico
    state = session.query(State).filter(State.id == 2).first()
    if state is not None:
        state.name = "New Mexico"
        session.commit()

    # closes the session and database connection
    session.close()
