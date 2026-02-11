from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.database import get_db
from app.models.user import User
from fastapi import Depends

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def get_current_user(db: Session = Depends(get_db)):
    user = db.query(User).first()

    if not user:
        user = User(
            email="dev@local",
            hashed_password=get_password_hash("dev-password")
        )
        db.add(user)
        db.commit()
        db.refresh(user)

    return user
