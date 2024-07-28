from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# --- Init DB for SQLite ---
db_url = "sqlite:///./test.db"  # SQLite database file path
engine = create_engine(db_url, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()