from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from mfriend.main import get_db
from  mfriend.auth import schemas, crud, exceptions
from mfriend.openapi import OpenApiTags

router = APIRouter(
    prefix="/api/auth",
    tags=[OpenApiTags.AUTH]
)

@router.post("/login")
def login(login: schemas.LoginSchema, db: Session = Depends(get_db)) -> schemas.UserReturnSchema:
    db_user = crud.get_user_by_id(db, login.id)
    
    if db_user == None:
        raise exceptions.UserNotFoundError(login.id)
    
    user_schema = schemas.UserSchema.from_orm(db_user)

    return schemas.UserReturnSchema(user=user_schema)

@router.post("/signup")
def signup(signup: schemas.SignupSchema, db: Session = Depends(get_db)) -> schemas.UserReturnSchema:
    db_user = crud.get_user_by_id(db, signup.id)

    if db_user != None:
        raise exceptions.UserAlreadyExistError(signup.id)
    
    user = crud.create_user(db, signup)
    
    user_schema = schemas.UserSchema.from_orm(user)
    return schemas.UserReturnSchema(user=user_schema)