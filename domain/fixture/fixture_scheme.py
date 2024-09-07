from pydantic import BaseModel

class Fixture(BaseModel):
    id: int
    korname: str
    engname: str
    player_id: int
    