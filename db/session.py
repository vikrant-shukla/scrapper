from contextvars import ContextVar

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

engine = create_engine("postgresql://vikrant:post1234@localhost:5432/postgres")

SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)
Base = declarative_base()

db_session: ContextVar[Session] = ContextVar("db_session", default=None)


def get_db():
    """get db"""
    if not db_session.get():
        db = SessionLocal()
        db_session.set(db)
        return db
    return db_session.get()
