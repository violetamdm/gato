#bases de datos SQL:
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from pydantic import BaseModel

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False)

class usuario(Base):
    __tablename__ = "meow_table"
    id = Column(Integer,primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    ip = Column(Integer, unique=True, index=True)

class user(BaseModel):
    ip: str
    nombre: str
