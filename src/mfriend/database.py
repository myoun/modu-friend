from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from mfriend.main import settings

Base = declarative_base()

engine = create_engine(settings.DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_table():
    Base.metadata.create_all(engine)

    
