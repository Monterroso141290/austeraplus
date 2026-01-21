from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.refresh_token import RefreshToken
from app.database import get_db
from app.schemas.user import UserCreate, UserOut
from app.crud.user import create_user, authenticate_user
from app.core.security import create_access_token, create_refresh_token
from jose import JWTError, jwt
from app.config import settings
from app.schemas.token import RefreshTokenRequest

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db, user.email, user.password)
    return db_user

@router.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    auth_user = authenticate_user(db, user.email, user.password)
    if not auth_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(
        data={"sub": str(auth_user.id)}
    )

    refresh_token = create_refresh_token(
        data={"sub": str(auth_user.id)}
    )

    db_token = RefreshToken(
        token=refresh_token,
        user_id=auth_user.id
    )
    db.add(db_token)
    db.commit()
    db.refresh(db_token)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }



@router.post("/refresh")
def refresh_token(
    data: RefreshTokenRequest,
    db: Session = Depends(get_db)
    ):
    try:
        print("SECRET:", settings.SECRET_KEY)
        print("ALGORITHM:", settings.ALGORITHM)
        print("TOKEN:", data.refresh_token)    

        payload = jwt.decode(
            data.refresh_token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        if payload.get("type") != "refresh":
            raise HTTPException(
                status_code=401,
                detail="Invalid token type"
            )

        user_id = int(payload.get("sub"))

        if user_id is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid Token"
            )

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Could not validate credentials"
        )

    db_token = db.query(RefreshToken).filter(
        RefreshToken.token == data.refresh_token,
        RefreshToken.revoked == False
    ).first()

    if not db_token:
        raise HTTPException(
            status_code=401,
            detail="Refresh token revoked or invalid"
        )

    db_token.revoked = True
    db.commit()

    new_access_token = create_access_token(
        data={"sub": str(user_id)}
    )
    new_refresh_token = create_refresh_token(
        data={"sub": str(user_id)}
    )

    db.add(RefreshToken(
        token=new_refresh_token,
        user_id=user_id
    ))
    db.commit()

    return {"access_token": new_access_token, "refresh_token": new_refresh_token}