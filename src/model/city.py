from sqlalchemy import Column
from sqlalchemy.types import String, UUID
from sqlalchemy.orm import declarative_base
import uuid

Base = declarative_base()

class City(Base):
    __tablename__ = 'city'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    code = Column(String, nullable=True)
    description = Column(String, nullable=True)