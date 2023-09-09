from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List
from mfriend.database import Base

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