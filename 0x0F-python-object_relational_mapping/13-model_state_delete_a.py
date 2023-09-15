#!/usr/bin/python3

"""
Deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa
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

     # Queries the database to retrieve all states containing the letter a and deletes them
    states = session.query(State).filter(State.name.like('%a%')).all()
    for state in states:
        session.delete(state)
    session.commit()

    # closes the session and database connection
    session.close()
