from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql.type_api import TypeEngine
from typing import Literal, List
from mfriend.database import Base

Personalities = Literal["bright", "sad"]

class User(Base):
    __tablename__ = "MODU_USERS"

    id = Column(String(16), primary_key=True, index=True)
    name = Column(String(16))
    hashed_password = Column(String(64))

    friends: Mapped[List["Friend"]] = relationship()
    

class Friend(Base):
    __tablename__ = "MODU_FRIENDS"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(16))

    friend: Mapped[String] = mapped_column(ForeignKey("MODU_USERS.id"))
    personalities: Mapped[List["FriendPersonality"]] = relationship()

class FriendPersonality(Base):
    __tablename__ = "MODU_FRIEND_PERSONALITIES"

    id = Column(Integer, primary_key=True, autoincrement=True)
    personality = Column(String(32))
    
    friend_id: Mapped[Integer] = mapped_column(ForeignKey("MODU_FRIENDS.id"))