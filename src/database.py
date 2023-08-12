from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Optional

_session: Optional[sessionmaker] = None
Base = declarative_base()

def connect(db_url: str) -> sessionmaker:
    global _session

    if _session == None:    
        engine = create_engine(db_url)
        _session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    return _session




