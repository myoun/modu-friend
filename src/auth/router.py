from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import get_db

router = APIRouter(
    prefix="/api/auth"
)