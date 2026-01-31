from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Budget(Base):
    __tablename__ = "budgets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="owned_budgets")
    categories = relationship("Category", back_populates="budget")
    transactions = relationship("Transaction", back_populates="budget")
    members = relationship("BudgetMember", back_populates="budget", cascade="all, delete")
