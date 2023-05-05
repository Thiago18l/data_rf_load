from sqlalchemy import Column
from sqlalchemy.types import String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class LegalNature(Base):
    __tablename__ = 'legal_nature'
    code = Column(String, primary_key=True, nullable=False, unique=True)
    description = Column(String, nullable=True)