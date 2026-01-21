#We import the library that will allow us to hash our passwords
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from jose import jwt
from app.config import settings

#We set up bcrypt. the crypt context will allow us to hash and verify every password.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#We transfrom a real password into a hashed one
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

#We validate the real password against the generated hash
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_minutes: int=60):
    #we copy the data to avoid modifying the new one
    to_encode = data.copy()

    #expiration time
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire, "type": "access"})

    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    return encoded_jwt

def create_refresh_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire, "type": "refresh"})
    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    print("SIGNING WITH SECRET:", settings.SECRET_KEY)
    print("SIGNING WITH ALGO:", settings.ALGORITHM)
    
    return encoded_jwt

