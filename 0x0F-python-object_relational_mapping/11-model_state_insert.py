#!/usr/bin/python3

"""
Adds the State object “Louisiana” to the database hbtn_0e_6_usa
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

     # Adds a new state to the database
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    #Prints the new state's id
    print(new_state.id)

    # closes the session and database connection
    session.close()
