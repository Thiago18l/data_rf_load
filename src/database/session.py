from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
import os


def get_session() -> Session:

    DATABASE_URL = os.getenv('DATABASE_URL')
    URL = DATABASE_URL.replace(
        'postgres://',
        'postgresql://',
        1
    )
    engine = create_engine(URL)
    Session = sessionmaker(bind=engine)
    return Session()
