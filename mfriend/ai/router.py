from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from mfriend.main import get_db
from  mfriend.ai import crud, models, schemas, exceptions
from mfriend.openapi import OpenApiTags
from uuid import UUID

router = APIRouter(
    prefix="/api/ai",
    tags=[OpenApiTags.AI]
)

@router.get("/friend")
def get_friend(friend_id: UUID, db: Session = Depends(get_db)) -> schemas.FriendSchema:
    db_friend = crud.get_friend_by_id(db, friend_id)
    if db_friend == None:
        raise exceptions.FriendNotFoundError(friend_id)
    
    friend = schemas.FriendSchema.from_orm(db_friend)

    return friend

@router.post("/friend")
def create_friend(friend_schema: schemas.CreateFriendSchema, db: Session = Depends(get_db)):
    db_friend = crud.create_friend(db, friend_schema)
    friend = schemas.FriendSchema.from_orm(db_friend)

    return friend

@router.get("/friend/conversation/")
def get_conversation():
    pass

