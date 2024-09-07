from pydantic import BaseModel

class Team(BaseModel):
    id: int
    kor_name: str
    team_id: int
    