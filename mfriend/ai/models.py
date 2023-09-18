from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List
from mfriend.database import Base

class Friend(Base):
    __tablename__ = "MODU_FRIENDS"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(16))
    mbti = Column(String(4))

    friend_of: Mapped[String] = mapped_column(ForeignKey("MODU_USERS.id"))