from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from mfriend.main import get_db
from  mfriend.auth import schemas, crud, exceptions

router = APIRouter(
    prefix="/api/auth",
)

@router.post("/login")
def login(login: schemas.LoginSchema, db: Session = Depends(get_db)) -> schemas.UserSchema:
    db_user = crud.get_user_by_id(db, login.id)
    
    if db_user == None:
        raise exceptions.UserNotFoundError(login.id)

    return db_user

@router.post("/signup")
def signup(signup: schemas.SignupSchema, db: Session = Depends(get_db)) -> schemas.UserSchema:
    db_user = crud.get_user_by_id(db, signup.id)

    if db_user:
        raise HTTPException(404, "해당 아이디를 사용하는 유저가 존재합니다.")
    
    user = crud.create_user(db, signup)
    
    user_schema = schemas.UserSchema.from_orm(user)
    return user_schema