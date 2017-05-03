from os import getenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine

base_class = declarative_base()


class Orders(base_class):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=False)
    contact_phone = Column(String(100))
    fmt_phone = Column(String(100))


def get_session():
    engine = create_engine(getenv('DB_URI'))
    session_class = sessionmaker(engine)
    return session_class()


if __name__ == '__main__':
    engine = create_engine(getenv('DB_URI'))
    base_class.metadata.create_all(engine)
