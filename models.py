from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

'''
Database Table Definition
'''

class Player(Base):
    __tablename__ = 'Player'
    id = Column(Integer, primary_key=True)
    pass

class Fixture(Base):
    __tablename__ = 'Fixture'
    id = Column(Integer, primary_key=True)
    pass

