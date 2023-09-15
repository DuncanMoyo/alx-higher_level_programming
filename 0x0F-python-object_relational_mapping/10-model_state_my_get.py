#!/usr/bin/python3

"""
Prints the State object with the name passed as argument from the database hbtn_0e_6_usa
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

    # Queries the database to retrieve the first state
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Prints the results in the format specified in the peompt
    if state is not None:
        print(state.id)
    else:
        print("Not found")

    # closes the session and database connection
    session.close()
