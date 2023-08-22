#!/usr/bin/python3
""" a script that lists the first State object from the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]))
    engine.connect()
    Session = sessionmaker(bind=engine)
    session = Session()
    first_obj = session.query(State).order_by(State.id).first()
    if first_obj:
        print(first_obj.id, ": ", first_obj.name, sep="")
    else:
        print()
