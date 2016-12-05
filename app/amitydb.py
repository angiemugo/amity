import os
import sys
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Rooms(Base):
        __tablename__ = 'rooms'
        room_name = Column(String(50))
        room_type = Column(String(50))
        person_id = Column(String(10), primary_key=True)
        person_name = Column(String(50))
        person_designation = Column(Text(50))



engine = create_engine('sqlite:///allrooms.sqlite')
Base.metadata.create_all(engine)