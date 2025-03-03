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

def get_fixtures_by_date(date: datetime, db: Session):
    start_date = date.replace(hour=6, minute=0, second=0, microsecond=0)
    end_date = start_date + timedelta(days=1)
    return_data = db.query(Fixture).filter(Fixture.date >= start_date, Fixture.date < end_date).order_by(Fixture.date.asc()).all()
    return return_data