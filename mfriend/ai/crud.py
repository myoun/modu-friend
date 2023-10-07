from sqlalchemy.orm import Session
from mfriend.ai import models, schemas
from uuid import UUID
from mfriend.ai.openai import chain, history

def get_friend_by_id(db: Session, friend_id: UUID) -> models.Friend | None:
    return db.query(models.Friend).get(friend_id)

def create_friend(db: Session, friend_info: schemas.CreateFriendSchema) -> models.Friend:
    friend_model = models.Friend(name=friend_info.name, mbti=friend_info.mbti, friend_of=friend_info.friend_of)
    db.add(friend_model)
    db.commit()
    db.refresh(friend_model)

    return friend_model

def get_chain(db: Session, friend_id: UUID):
    friend = get_friend_by_id(db, friend_id)

    if friend == None:
        raise Exception("Cannot find user.") # TODO: Change Exception

    llm_chain = chain.get_chain(db, friend)
    return llm_chain

def get_conversation(db: Session, friend_id: UUID):
    llm_chain = get_chain(db, friend_id)
    memory = llm_chain.memory
    
    if memory == None:
        return None
    
    raw_conversation = memory.dict()["chat_memory"].messages

    conversation = []

    return conversation