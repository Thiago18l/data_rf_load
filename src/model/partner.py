import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Partner(Base):
    __tablename__ = 'partner'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    cnpjBasic = Column(String, nullable=True)
    partnerIdentifier = Column(String, nullable=True)
    partnerName = Column(String, nullable=True)
    cpfOrCnpjPartner = Column(String, nullable=True)
    partnerQualification = Column(String, nullable=True)
    entryDataSociety = Column(String, nullable=True)
    country = Column(String, nullable=True)
    procurator = Column(String, nullable=True)
    procuratorName = Column(String, nullable=True)
    procuratorQualification = Column(String, nullable=True)
    ageGroup = Column(String, nullable=True)
