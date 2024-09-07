from sqlalchemy.orm import Session
from models import Fixture
from datetime import datetime, timedelta

def get_fixture_data_by_id(fixture_id: int, db:Session):
    return_data = db.query(Fixture).filter(Fixture.fixture_id == fixture_id).first()
    return return_data

def get_fixtures_by_date_and_league(league_id: int, date: datetime, db:Session):
    return_data = db.query(Fixture).filter(Fixture.league_id == league_id, Fixture.date > date + timedelta(hours=6),\
        Fixture.date < date + timedelta(days=1, hours=6)).order_by(Fixture.date.asc()).all()
    return return_data