from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from mfriend.main import get_db
from  mfriend.ai import crud, models, schemas, exceptions
from mfriend.auth import crud as auth_crud, schemas as auth_schema
from mfriend.openapi import OpenApiTags
from uuid import UUID

router = APIRouter(
    prefix="/api/ai",
    tags=[OpenApiTags.AI]
)

@router.get("/friend/info")
def get_friend(friend_id: UUID, db: Session = Depends(get_db)) -> schemas.FriendSchema:
    db_friend = crud.get_friend_by_id(db, friend_id)
    if db_friend == None:
        raise exceptions.FriendNotFoundError(friend_id)
    
    friend = schemas.FriendSchema.from_orm(db_friend)

    return friend

@router.post("/friend")
def create_friend(create_friend_schema: schemas.CreateFriendSchema, db: Session = Depends(get_db)):
    db_friend = crud.create_friend(db, create_friend_schema)
    friend = schemas.FriendSchema.from_orm(db_friend)

    return friend

@router.get("/friend/conversation/")
def get_conversation(friend_id: UUID, db: Session = Depends(get_db)):
    conversations = crud.get_conversation(db, friend_id)
    
    if conversations == None:
        raise HTTPException(404, "Conversation Not Found")
    
    return conversations


@router.post("/friend/conversation/")
def toss_message_and_response(toss_message_schema: schemas.TossMessageSchema, db: Session = Depends(get_db)):
    chain = crud.get_chain(db, toss_message_schema.friend_id)

    inputs = {
        "message": toss_message_schema.message
    }

    response_message = chain.run(inputs)

    response = {
        "message": response_message
    }

    return response