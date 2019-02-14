from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customers'

    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(200))
    surname = Column(String(200))
