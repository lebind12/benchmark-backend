from models import Player
from sqlalchemy.orm import Session

def get_player_data_by_id(db: Session, player_id: int):
    db_playerId = db.query(Player).filter(Player.player_id == player_id).first()
    return db_playerId

def get_lineup_data_by_teamid(db:Session, team_id: int):
    db_lineupData = db.query(Player).filter(Player.team_id == team_id).all()
    returnData = {}
    for item in db_lineupData:
        returnData[item.player_id] = item.kor_short_name
    return returnData