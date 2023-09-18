from sqlalchemy.orm import Session
from mfriend.ai import models, schemas

def get_friend_by_id(db: Session, friend_id: int) -> models.Friend | None:
    return db.query(models.Friend).get(friend_id)

def create_friend(db: Session, friend_info: schemas.CreateFriendSchema) -> models.Friend:
    friend_model = models.Friend(name=friend_info.name, mbti=friend_info.mbti, friend_of=friend_info.friend_of)
    db.add(friend_model)
    db.commit()
    db.refresh(friend_model)

    return friend_model

