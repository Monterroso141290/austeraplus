from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import settings

engine = create_engine(settings.DATABASE_URL, echo=False, future=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    #A new session is created for a new request
    db = SessionLocal()
    try:
        #the database is given to the endpoint
        yield db
    finally:
        #The session closes no matter what happens
        db.close()