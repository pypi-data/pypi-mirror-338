
from fastapi import Depends, status, Response, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from pydantic import BaseModel
import models
from .auth_token import verify_token
from database import get_db
from sqlmodel import Session, select
from models.UserModel import User 
from uuid import UUID


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user_cookie(request: Request, db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials", 
        headers={"WWW-Authenticate": "Bearer"},
    ) 
  
    token = request.cookies.get("access_token")
    if not token:
        raise credentials_exception
    token_data = verify_token(token)
    
    user = db.exec(select(User).where(User.id == UUID(token_data.user_id))).first()
    if not user:
        raise credentials_exception

    return user



def get_current_user_oauth(request: Request, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials", 
        headers={"WWW-Authenticate": "Bearer"},
    ) 
 
    token_data = verify_token(token)
    
    user = db.exec(select(User).where(User.id == UUID(token_data.user_id))).first()
    if not user:
        raise credentials_exception

    return user