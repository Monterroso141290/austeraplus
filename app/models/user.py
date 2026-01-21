from sqlalchemy import Column, Integer, String
from app.database import Base

#User table in the database
class User(Base):
    #name of the table
    __tablename__="users"

    #This is the user ID.
    id = Column(Integer, primary_key=True, index=True)
    #This is the user email, and it will be unique to avoid duplicates
    email = Column(String, unique=True, nullable=False, index = True)
    #We save the password as a hash
    hashed_password = Column(String, nullable=False)

    budget_members = relationship(
        "BudgetMember",
        back_populates="user",
        cascade="all, delete"
    )