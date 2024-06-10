from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

import os
load_dotenv()

POSTGRES_SERVER_IP = os.getenv("POSTGRES_SERVER_IP")
POSTGRES_SERVER_PORT = os.getenv("POSTGRES_SERVER_PORT")
POSTGRES_DATABASE_NAME = os.getenv("POSTGRES_DATABASE_NAME")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")

SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER_IP}:{POSTGRES_SERVER_PORT}/{POSTGRES_DATABASE_NAME}"

if SQLALCHEMY_DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
else:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()