from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, Mapped
from typing import List
from mfriend.ai.models import Friend
from mfriend.database import Base

class User(Base):
    __tablename__ = "MODU_USERS"

    id = Column(String(16), primary_key=True, index=True)
    name = Column(String(16))
    hashed_password = Column(String(64))
    salt = Column(String(32))

    friends: Mapped[List["Friend"]] = relationship()