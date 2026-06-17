from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, primary_key=False, index=False, nullable=False)
    email = Column(String, nullable=False)
    expense = relationship('Expense', back_populates="user")

class Expense(Base):
    __tablename__ = "expenses"
    id= Column(Integer, primary_key=True, index=True)
    desc=Column(String)
    amount=Column(Integer, nullable=False)
    expense_date=Column(Date)
    user_id=Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship('User', back_populates="expense")