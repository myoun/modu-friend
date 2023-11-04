from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from mfriend.database import Base
from mfriend.data_types import BinaryUUID
from uuid import uuid4

class Friend(Base):
    __tablename__ = "MODU_FRIENDS"

    id = Column('id', BinaryUUID, primary_key=True, default=uuid4)
    name = Column(String(16))
    mbti = Column(String(4))
    gender = Column(String(6))

    friend_of: Mapped[String] = mapped_column(ForeignKey("MODU_USERS.id"))