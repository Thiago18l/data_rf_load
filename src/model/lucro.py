from sqlalchemy import Column, UniqueConstraint
from sqlalchemy.types import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
import uuid

Base = declarative_base()

class Lucro(Base):
    __tablename__ = 'real_lucro'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    cnpj = Column(String, nullable=True)
    year = Column(String, nullable=True)
    cnpjSCP = Column(String, nullable=True)
    formTaxation = Column(String, nullable=True)
    amountScriptures = Column(String, nullable=True)

    __table_args__ = (UniqueConstraint('cnpj', 'year', 'cnpjSCP', 'formTaxation'), {})