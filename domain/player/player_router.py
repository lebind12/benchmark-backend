from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import Player
from database import get_db
from domain.player.player_scheme import Player
from domain.player.player_crud import get_player_data_by_id, get_lineup_data_by_teamid

router = APIRouter(
    prefix="/api/match"
)

@router.get("/player")
def get_player_data(player_id: int, db: Session = Depends(get_db)):
    data = get_player_data_by_id(player_id=player_id, db=db)
    return data

@router.get("/player/lineup")
def get_lineup_data(team_id: int, db:Session = Depends(get_db)):
    data = get_lineup_data_by_teamid(team_id=team_id, db=db)
    return data