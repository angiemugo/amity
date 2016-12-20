import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Person(Base):
	__tablename__ = 'employee'
	id = Column(Integer, primary_key=True, autoincrement=True)
	person_name = Column(String, nullable=False)
	person_description = Column(String, nullable=False)
	wants_accomodation = Column(String, nullable=True)


class Room(Base):
	"""creates the rooms table
	"""
	__tablename__ = 'room'
	id = Column(Integer, primary_key=True, autoincrement=True)
	room_name = Column(String(20), nullable=False)
	room_type = Column(String(20), nullable=False)
	capacity = Column(Integer, nullable=False)


class OfficeAllocations(Base):
	"""creates a table to store office allocations"""
	__tablename__ = "office_allocations"
	id = Column(Integer, primary_key=True, autoincrement=True)
	room_name = Column(String(20), nullable=False)
	room_members = Column(String(250))


class LSpaceAllocations(Base):
	"""Store living space allocations"""
	__tablename__ = "lspace_allocations"
	id = Column(Integer, primary_key=True, autoincrement=True)
	room_name = Column(String(20), nullable=False)
	room_members = Column(String(250))


class DatabaseCreator(object):
	"""Creates a db connection object"""

	def __init__(self, db_name=None):
		self.db_name = db_name
		if self.db_name:
			self.db_name = db_name + '.sqlite'
		else:
			self.db_name = 'main.sqlite'
		self.engine = create_engine('sqlite:///' + self.db_name)
		self.session = sessionmaker()
		self.session.configure(bind=self.engine)
