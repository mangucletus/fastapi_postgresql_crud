from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from app import models, schemas, crud, database
from contextlib import asynccontextmanager
from app import init_db


# Initialize FastAPI
app = FastAPI()


# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the database
#init_db()  # Call the init_db function to create tables


# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI!"}


# Lifespan context manager for startup and shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    database.Base.metadata.create_all(bind=database.engine)
    await database.connect()
    print("Database tables created successfully.")
    
    yield  # This is where FastAPI handles the requests
    
    # Shutdown
    await database.disconnect()

app.lifespan = lifespan


@app.get("/users/")
async def read_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

# User registration endpoint
@app.post("/users/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.create_user(db=db, user=user)
    if db_user is None:
        raise HTTPException(status_code=400, detail="User already exists")
    return db_user












