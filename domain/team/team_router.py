from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import Team
from database import get_db
from domain.team.team_crud import get_team_name_by_id

router = APIRouter(
    prefix="/api/match"
)

@router.get("/team")
def get_player_data(team_id: int, db: Session = Depends(get_db)):
    data = get_team_name_by_id(team_id=team_id, db=db)
    return data