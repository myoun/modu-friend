from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from mfriend.main import get_db
from  mfriend.ai import crud, schemas, exceptions, model
from mfriend.openapi import OpenApiTags

router = APIRouter(
    prefix="/api/ai",
    tags=[OpenApiTags.AI]
)

@router.get("/friend/{friend_id}")
def get_friend(friend_id: int, db: Session = Depends(get_db)) -> schemas.FriendSchema:
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
