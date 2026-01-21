from pydantic import BaseModel, EmailStr

# Schema to receive user data
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# Schema to return user data
class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True 
