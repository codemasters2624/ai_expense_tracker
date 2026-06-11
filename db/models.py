from sqlalchemy import Column, Integer, String
from db.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, primary_key=False, index=False, nullable=False)
    email = Column(String, nullable=False)

class Expense(Base):
    __tablename__ = "expense"
    id= Column(Integer, primary_key=True, index=True)
    desc=Column(String, nullable=False)