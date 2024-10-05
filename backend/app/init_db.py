# init_db.py
from app.database import engine, Base

# This will create the database tables based on the defined models
Base.metadata.create_all(bind=engine)

print("Database tables created successfully.")
