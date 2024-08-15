from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import Fixture
from database import get_db


router = APIRouter(
    prefix="/api/match"
)