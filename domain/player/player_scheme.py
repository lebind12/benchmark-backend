from pydantic import BaseModel

class Player(BaseModel):
    id: int
    korname: str
    engname: str
    player_id: int
    