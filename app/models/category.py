from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    # 🔗 THIS NOW HAS A VALID FK TARGET
    expenses = relationship(
        "Expense",
        back_populates="category",
        cascade="all, delete-orphan"
    )
