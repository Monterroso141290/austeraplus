from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    budget_id = Column(Integer, ForeignKey("budgets.id"))

    budget = relationship("Budget", back_populates="categories")