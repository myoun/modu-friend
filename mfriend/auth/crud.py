from sqlalchemy.orm import Session
from mfriend.auth import models, schemas

def get_user_by_id(db: Session, id: str) -> models.User | None:
    return db.query(models.User).get(id)
    
def create_user(db: Session, schema: schemas.SignupSchema) -> models.User:
    db_user = models.User(id=schema.id, name=schema.name, hashed_password=schema.hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user  