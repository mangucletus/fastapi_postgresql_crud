from sqlalchemy.orm import Session
from app import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    # Check if the user already exists
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        return None  # User already exists

    db_user = models.User(username=user.username, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
