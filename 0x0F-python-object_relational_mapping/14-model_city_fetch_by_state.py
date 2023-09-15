#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa sorted in ascending order by cities.id
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys


if __name__ == "__main__":
    # Connects to the MySQL server running on localhost at port 3306
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Creates a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Queries the database to retrieve all cities and their states
    cities = session.query(City).order_by(City.id).all()

    # Prints the results in the format specified in the prompt
    for city in cities:
        state_name = session.query(State).filter(
            State.id == city.state_id
        ).first().name
        print("{}: ({}) {}".format(state_name, city.id, city.name))

    # Closes the session and database connection
    session.close()
