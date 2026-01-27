from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Budget(Base):
    __tablename__ = "budgets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    #Relationships
    members = relationship(
        "BudgetMember",
        back_populates="budget",
        cascade="all, delete"
    )

    categories = relationship(
        "Category",
        back_populates="budget",
        cascade="all, delete"
    )

    transactions = relationship(
        "Transaction",
        back_populates="budget",
    )