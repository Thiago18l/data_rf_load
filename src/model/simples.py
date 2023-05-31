from sqlalchemy import Column
from sqlalchemy.types import String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Simples(Base):
    __tablename__ = 'national_simples'

    cnpj = Column(String, primary_key=True, nullable=True)
    simplesOption = Column(String, nullable=True)
    dateSimplesOption = Column(String, nullable=True)
    dateExclusionSimplesOption = Column(String, nullable=True)
    optionMei = Column(String, nullable=True)
    dateOptionMei = Column(String, nullable=True)
    dateExclusionOptionMei = Column(String, nullable=True)
