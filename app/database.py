"""
database.py
-----------
This file sets up everything needed to talk to PostgreSQL using SQLAlchemy.

It creates:
1. An "engine" -> the actual connection to the PostgreSQL database.
2. A "SessionLocal" factory -> used to create individual database sessions
   (a session is like a temporary workspace for talking to the DB).
3. A "Base" class -> all our database models (tables) will inherit from this.
4. A "get_db()" dependency -> FastAPI will call this for every request that
   needs database access, and it makes sure the session is always closed
   properly afterwards.
"""

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Load variables from the .env file (like DATABASE_URL) into the environment
load_dotenv()

# Read the database URL from the environment. This keeps the password
# out of the source code.
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError(
        "DATABASE_URL is not set. Make sure you have a .env file "
        "with DATABASE_URL=postgresql://postgres:admin@localhost:5432/task_management"
    )

# The engine is the core object SQLAlchemy uses to communicate with PostgreSQL.
engine = create_engine(DATABASE_URL)

# SessionLocal is a "session factory". Every time we call SessionLocal(),
# we get a new database session to work with.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base is the parent class that all our SQLAlchemy models (tables) will
# inherit from. SQLAlchemy uses this to know which classes represent tables.
Base = declarative_base()


def get_db():
    """
    FastAPI dependency that provides a database session to a route,
    and guarantees the session is closed afterwards -- even if an
    error happens while handling the request.

    Usage in a route:
        def some_route(db: Session = Depends(get_db)):
            ...
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
