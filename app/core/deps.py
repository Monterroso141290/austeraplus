# deps.py
# This will be a Token Reader that will validate it existes and will show it to the button in SwaggerUI
from fastapi.security import OAuth2PasswordBearer
#Depends will inject dependencies into path operations, HTTPException is used to raise HTTP errors, status contains HTTP status codes
from fastapi import Depends, HTTPException, status
#JWTError will catch invalid tokens, and jwt will decode the tokens
from jose import JWTError, jwt
#The session that will be used to interact with the database we'll create.
from sqlalchemy.irm import Session

#Importing our own modules, secret key and algotitmhms from config, get_db to get a database session, and User model to query users.
from app.config import Settings
from app.database import get_db
from app.models.user import User

#This will tell our FastAPI app that it uses Bearer tokens for authentication and will tell Swagger where tokens come from. This line
#does not verify anything, it only extracts the token that already exists from the request. 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(
    #JWT that is extracted from the header
    token: str = Depends(oauth2_scheme),
    #Database session. It Auto-opens and closes the database for us.
    db: Session = Depends(get_db),):

    settings = Settings()

    #We use this exception to avoid repetition, and we can have the same error for missing tokens, invalid tokens, expired tokens, and users not found.
    #This is a required Header by OAuth2 standard.
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    #this case checks if the token is modified, if its expired or of the secret key is wrong. A JWTError will be raised in those cases.
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

    #The "sub" field is a standard JWT field that contains the subject of the token, in our case, the user ID.
    user_id: int | None = payload.get("sub")

    #We raise an error and avoid a crash
    if user_id is None:
        raise credentials_exception

    #If the token is invalid, we catch the error and raise our HTTP exception
    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        raise credentials_exception

    return user