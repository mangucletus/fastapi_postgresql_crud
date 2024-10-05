from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .. import models, schemas, crud, database

# Use a test-specific database URL here
DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

models.Base.metadata.create_all(bind=engine)

def test_create_user():
    db = TestingSessionLocal()
    user_data = schemas.UserCreate(username="testuser", email="test@example.com", password="password")
    user = crud.create_user(db, user_data)
    assert user.username == "testuser"
