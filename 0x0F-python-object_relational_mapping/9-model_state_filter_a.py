#!/usr/bin/python3
""" a script that lists all State objects from the database hbtn_0e_6_usa.
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
    qry = session.query(State).filter(
          State.name.like('%a%')).order_by(State.id)
    for row in qry:
        print(row.id, ': ', row.name, sep='')
