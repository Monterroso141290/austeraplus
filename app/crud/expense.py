from sqlalchemy.orm import Session
from app.models.expense import Expense
from app.models.user import User
from app.core.security import hash_password, verify_password
from app.schemas.expense import ExpenseCreate

#We read all the expenses from the database
def get_expenses(db: Session):
    return db.query(Expense).all()

#We create a new expense
def create_expense(db: Session, expense: ExpenseCreate):
    new_expense = Expense(
        title=expense.title,
        amount=expense.amount,
        category=expense.category
    )

    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)

    return new_expense

#We will read an expense by ID
def get_expense_by_id(db:Session, expense_id: int):
    return db.query(Expense).filter(Expense.id == expense_id).first()

#Allows to delete an expense
def delete_expense(db:Session, expense_id:int):
    expense = get_expense_by_id(db, expense_id)

    if expense != None:
        db.delete(expense)
        db.commit()

    return expense

def create_user(db: Session, email: str, password: str):
    hashed = hash_password(password)
    user = User(email=email, hashed_password=hashed)
    db.add(user)
    db.commit()
    #We refresh to get the new User ID
    db.refresh(user)
    return user

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user
