# app/dependencies.py

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User

def get_current_user(db: Session = Depends(get_db)) -> User:
    # TEMPORARY: return first user (for development only)
    user = db.query(User).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated"
        )

    return user
