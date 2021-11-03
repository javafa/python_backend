from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base) :
    __tablename__ = "user"
    id            = Column(Integer,     nullable=False, primary_key=True, autoincrement=True)
    email         = Column(String(255), nullable=False, index=True, unique=True)
    name          = Column(String(5),   nullable=False, index=True)
    age           = Column(Integer,     nullable=True)
    gender        = Column(String(1),   nullable=True)
    address       = Column(String(200), nullable=True)
    tel           = Column(String(11),  nullable=True)
    created_at    = Column(DateTime,    nullable=False, default=func.utc_timestamp())
    updated_at    = Column(DateTime,    nullable=False, default=func.utc_timestamp(), onupdate=func.utc_timestamp())
