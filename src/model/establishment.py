from sqlalchemy import Column
from sqlalchemy.types import String, UUID
from sqlalchemy.orm import declarative_base
import uuid

Base = declarative_base()

class Establishment(Base):
    __tablename__ = 'establishment'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    taxpayerRegistry = Column(String, unique=True, nullable=True)
    cnpjOrder = Column(String, nullable=True)
    cnpjDv = Column(String, nullable=True)
    branchIdentifier = Column(String, nullable=True)
    fantasyName = Column(String, nullable=True)
    cadastralSituation = Column(String, nullable=True)
    dateCadastralSituation = Column(String, nullable=True)
    reasonCadastralSituation = Column(String, nullable=True)
    outsideCityName = Column(String, nullable=True)
    country = Column(String, nullable=True)
    startDateActivity = Column(String, nullable=True)
    principalCNAEFiscal = Column(String, nullable=True)
    secondaryCNAEFiscal = Column(String, nullable=True)
    typeOfStreet = Column(String, nullable=True)
    street = Column(String, nullable=True)
    number = Column(String, nullable=True)
    complement = Column(String, nullable=True)
    neighborhood = Column(String, nullable=True)
    cep = Column(String, nullable=True)
    UF = Column(String, nullable=True)
    city = Column(String, nullable=True)
    ddd1 = Column(String, nullable=True)
    phone1 = Column(String, nullable=True)
    ddd2 = Column(String, nullable=True)
    phone2 = Column(String, nullable=True)
    faxDDD = Column(String, nullable=True)
    fax = Column(String, nullable=True)
    email = Column(String, nullable=True)
    specialSituation = Column(String, nullable=True)
    dateSpecialSituation = Column(String, nullable=True)
