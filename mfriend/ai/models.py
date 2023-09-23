from sqlalchemy import Column, ForeignKey, Integer, String, BINARY
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List
from mfriend.database import Base
from mfriend.data_types import BinaryUUID
from uuid import uuid4

class Friend(Base):
    __tablename__ = "MODU_FRIENDS"

    id = Column('id', BinaryUUID, primary_key=True, default=uuid4)
    name = Column(String(16))
    mbti = Column(String(4))

    friend_of: Mapped[String] = mapped_column(ForeignKey("MODU_USERS.id"))