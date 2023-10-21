from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from mfriend.main import get_db
from  mfriend.auth import schemas, crud, exceptions, util
from mfriend.openapi import OpenApiTags

router = APIRouter(
    prefix="/api/auth",
    tags=[OpenApiTags.AUTH]
)

@router.get("/user")
def get_user_info(user_id: str, db: Session = Depends(get_db)) -> schemas.UserReturnSchema:
    db_user = crud.get_user_by_id(db, user_id)
    
    if db_user == None:
        raise exceptions.UserNotFoundError(user_id)
    
    user_schema = schemas.UserSchema.from_orm(db_user)

    return schemas.UserReturnSchema(user=user_schema)

@router.post("/login")
def login(login: schemas.LoginSchema, db: Session= Depends(get_db)) -> schemas.UserReturnSchema:
    db_user = crud.get_user_by_id(db, login.id)
    
    if db_user == None:
        raise exceptions.UserNotFoundError(login.id)
    
    user_schema = schemas.UserAuthSchema.from_orm(db_user)

    if (util.is_correct_password(user_schema.salt, user_schema.hashed_password, login.password)):
        return schemas.UserReturnSchema(user=schemas.UserSchema.from_orm(db_user))
    else:
        raise exceptions.PasswordIncorrectError(login.id)


@router.post("/user")
def create_user(signup: schemas.SignupSchema, db: Session = Depends(get_db)) -> schemas.UserReturnSchema:
    db_user = crud.get_user_by_id(db, signup.id)

    if db_user != None:
        raise exceptions.UserAlreadyExistError(signup.id)
    
    user = crud.create_user(db, signup)
    
    user_schema = schemas.UserSchema.from_orm(user)
    return schemas.UserReturnSchema(user=user_schema)