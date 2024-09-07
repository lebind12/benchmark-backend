from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Fixture
from database import get_db
from domain.fixture import fixture_crud
from datetime import datetime


router = APIRouter(
    prefix="/api/match"
)

@router.get("/fixture")
def get_fixture_data(fixture_id: int = None, date:datetime = None, league_id:int = None,  db: Session = Depends(get_db)):
    if fixture_id:
        return fixture_crud.get_fixture_data_by_id(fixture_id=fixture_id, db=db)
    elif date and league_id:
        return fixture_crud.get_fixtures_by_date_and_league(league_id=league_id, date=date, db=db)
    else:
        raise HTTPException(status_code=400, detail="query not ok")