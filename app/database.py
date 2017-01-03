import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Employee(Base):

    """Creates people table"""
    __tablename__ = 'employee'
    person_id = Column(Integer, primary_key=True, autoincrement=True)
    person_name = Column(String, nullable=False)
    person_description = Column(String, nullable=False)
    wants_accommodation = Column(String, nullable=True)
    office_allocated = Column(String, nullable=True)
    lspace_allocated = Column(String, nullable=True)


class Room(Base):
    """Creates room table"""
    __tablename__ ='rooms'
    room_id = Column(Integer, primary_key=True, autoincrement=True)
    room_name = Column(String, nullable=False)
    room_type = Column(String, nullable=False)
    occupants = Column(Integer, nullable=False)
    max_occupants = Column(Integer, nullable=False)

def create_db(db_name):
    db = db_name + '.db'
    engine = create_engine('sqlite:///' + db)
    Base.metadata.create_all(engine)

    return engine



create_db('somedb')
