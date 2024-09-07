from models import Team
from sqlalchemy.orm import Session

def get_team_name_by_id(db: Session, team_id: int):
    db_teamName = db.query(Team).filter(Team.player_id == team_id).first()
    return db_teamName