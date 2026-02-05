from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)

    budget_id = Column(Integer, ForeignKey("budgets.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    budget = relationship("Budget", back_populates="transactions")
    user = relationship("User")
