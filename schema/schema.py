from sqlalchemy import Column, INTEGER, VARCHAR, TEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ScrapperSchema(Base):
    """only for migrations"""
    __tablename__ = "scrap_registration_table"
    __table_args__ = {"schema": "scrap"}

    Id = Column(INTEGER, primary_key=True)
    registration_id = Column(TEXT)
    Name = Column(VARCHAR(100))
    Address = Column(TEXT)
    Correspondence_Address = Column(TEXT)
    Validity = Column(VARCHAR(500))
