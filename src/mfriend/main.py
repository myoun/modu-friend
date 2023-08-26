from fastapi import FastAPI
from mfriend.config import Settings
from contextlib import asynccontextmanager

settings = Settings()

def get_db():
    from mfriend.database import SessionLocal
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@asynccontextmanager
async def lifespan(app: FastAPI):
    from mfriend.database import create_table
    create_table()
    yield

app = FastAPI(lifespan=lifespan)

def use_router():
    from mfriend.auth.router import router as auth_router
    app.include_router(auth_router)

use_router()