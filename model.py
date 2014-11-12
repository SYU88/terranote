from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session
from datetime import datetime
# import quake

engine = create_engine("sqlite:///terranote.db", echo=False)
session = scoped_session(sessionmaker(bind=engine,
                                      autocommit = False,
                                      autoflush = False))

Base = declarative_base()
Base.query = session.query_property()

### Class declarations go here
class Quake(Base):
    """ from quake.py """  
    __tablename__ = "quakes"

    # id = Column(Integer, primary_key = True)
    quake_id = Column(String(50), primary_key = True)
    title = Column(String(400), nullable = False)
    quake_type = Column(String(25), nullable = False)
    magnitude = Column(Float, nullable = False)
    place = Column(String(500), nullable = False)
    latitude = Column(Float, nullable = False)
    longtitude = Column(Float, nullable = False)
    depth = Column(Float, nullable = False)
    quake_datetime = Column(DateTime, nullable = False)
    url = Column(String, nullable = False)
    seismictype = Column(String, nullable = False)
    status = Column(String, nullable = False)
    felt = Column(Integer, nullable = True)
    tsunami = Column(Integer, nullable = True)
    recordtime = Column(DateTime, nullable = False)

### End class declarations

# def connect():
#     global ENGINE
#     global Session

#     ENGINE = create_engine("sqlite:///terranote.db", echo=True)
#     Session = sessionmaker(bind=ENGINE)

#     return Session()

def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()

