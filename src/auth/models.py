from sqlalchemy import Column, ForeignKey, Integer, String, UUID
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql.type_api import TypeEngine
from typing import Literal, List
from ..database import Base

Personalities = Literal["bright", "sad"]

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    hashed_password = Column(String)

    friends: Mapped[List["Friend"]] = relationship()
    

class Friend(Base):
    __tablename__ = "friends"

    id = Column(UUID, primary_key=True, index=True)
    name = Column(String)

    friend: Mapped[String] = mapped_column(ForeignKey("users.id"))
    personalities: Mapped[List["FriendPersonality"]] = relationship()

class FriendPersonality(Base):
    __tablename__ = "friend_personalities"

    id = Column(Integer, primary_key=True, autoincrement=True)
    personality = Column(TypeEngine[Personalities])
    
    friend_id: Mapped[UUID] = mapped_column(ForeignKey("friends.id"))