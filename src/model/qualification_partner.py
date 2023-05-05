from sqlalchemy import Column
from sqlalchemy.types import String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class QualificationPartner(Base):
    __tablename__ = 'qualification_partner'
    code = Column(String, primary_key=True, unique=True)
    description = Column(String, nullable=True)