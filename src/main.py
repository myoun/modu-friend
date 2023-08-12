from fastapi import FastAPI
from .config import Settings
from .database import Base, engine, SessionLocal

settings = Settings()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()