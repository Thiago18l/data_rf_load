from sqlalchemy import Column, String, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Company(Base):
    __tablename__ = 'company'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    taxpayerRegistry = Column(String, unique=True, nullable=True)
    businessName = Column(String, unique=True, nullable=True)
    legalNature = Column(String, unique=True, nullable=True)
    responsibleQualification = Column(String, unique=True, nullable=True)
    capitalCompany = Column(String, unique=True, nullable=True)
    sizeCompany = Column(String, unique=True, nullable=True)
    responsibleEntityFederative = Column(String, unique=True, nullable=True)

    __table_args__ = (UniqueConstraint('taxpayerRegistry'), UniqueConstraint('businessName'), UniqueConstraint('legalNature'), UniqueConstraint(
        'responsibleQualification'), UniqueConstraint('capitalCompany'), UniqueConstraint('sizeCompany'), UniqueConstraint('responsibleEntityFederative'), {})
