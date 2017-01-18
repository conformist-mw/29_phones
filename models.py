from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=False)
    contact_name = Column(String(200))
    contact_phone = Column(String(100))
    contact_email = Column(String(150))
    status = Column(String)
    created = Column(String)
    confirmed = Column(String)
    comment = Column(String)
    price = Column(String)
