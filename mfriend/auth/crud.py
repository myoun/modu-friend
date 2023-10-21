from sqlalchemy.orm import Session
from mfriend.auth import models, schemas, util

def get_user_by_id(db: Session, id: str) -> models.User | None:
    return db.query(models.User).get(id)
    
def create_user(db: Session, schema: schemas.SignupSchema) -> models.User:
    salt, hashed_password = util.hash_new_password(schema.password)
    db_user = models.User(id=schema.id, name=schema.name, hashed_password=hashed_password.hex(), salt=salt.hex())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user  