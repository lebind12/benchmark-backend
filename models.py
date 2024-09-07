from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

'''
Database Table Definition
'''

class Fixture(Base):
    __tablename__ = 'Fixture'
    id = Column(Integer, primary_key=True)
    roundname = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    fixture_id = Column(Integer, nullable=False)
    venue = Column(String, nullable=False)
    eng_homename = Column(String, nullable=False)
    eng_awayname = Column(String, nullable=False)
    kor_homename = Column(String, nullable=False)
    kor_awayname = Column(String, nullable=False)
    home_id = Column(Integer, nullable=False)
    away_id = Column(Integer, nullable=False)
    status = Column(String, nullable=False)
    league_name = Column(String, nullable=False)
    league_id = Column(Integer, nullable=False)

class Player(Base):
    __tablename__ = 'Player'
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, nullable=False)
    eng_player_name = Column(String, nullable=False)
    kor_player_name = Column(String, nullable=False)
    kor_short_name = Column(String, nullable=False)
    player_age = Column(String, nullable=True)
    player_shirt_number = Column(String, nullable=True)
    face_url = Column(String, nullable=False)
    team_id = Column(Integer, nullable=False)

class Team(Base):
    __tablename__ = "Team"
    id = Column(Integer, primary_key=True)
    team_id = Column(Integer, nullable=False)
    kor_team_name = Column(String, nullable=False)
    eng_team_name = Column(String, nullable=False)