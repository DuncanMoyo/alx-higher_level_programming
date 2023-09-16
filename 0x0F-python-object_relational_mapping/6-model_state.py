#!/usr/bin/python3
"""
contains the class definition of a State and an instance Base
= declarative_base():instance Base = declarative_base():
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    arg3 = sys.argv[3]
    db = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(db.format(arg1, arg2, arg3), pool_pre_ping=True)
    Base.metadata.create_all(engine)
