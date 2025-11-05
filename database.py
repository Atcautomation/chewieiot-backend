from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os

DB_URL = os.getenv("DATABASE_URL", "sqlite:///./chewieiot.db")

if DB_URL.startswith("postgres://"):
    DB_URL = DB_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    Base.metadata.create_all(bind=engine)
