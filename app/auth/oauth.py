from jose import JWTError, jwt
from datetime import datetime, timedelta
from ..schemas import user_schemas
from ..db import database, database_models
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from ..environment_config import settings

oauth_scheme = OAuth2PasswordBearer(tokenUrl='login')

# SECRET_KEY
SECRET_KEY = settings.secret_key

# Algorithm
ALGORITHM = settings.algorithm

# Expiration in minutes
ACCESS_TOKEN_EXPIRATION_MINUTES = settings.access_token_expiration_in_minutes

def create_access_token(data: dict):
    data_to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRATION_MINUTES)
    data_to_encode.update({"exp":expire})

    token = jwt.encode(data_to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return token


def verify_access_token(token: str, credentials_exception):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        id: str = payload.get("userId")
        if id is None:
            raise credentials_exception
        token_data = user_schemas.TokenData(id=id)
    except JWTError:
        raise credentials_exception
    

    return token_data


def get_current_user(token: str = Depends(oauth_scheme), db: Session = Depends(database.get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Action not Authorized", headers={"WWW-Authenticate":"Bearer"})

    token_data = verify_access_token(token, credentials_exception)

    user: database_models.User = db.query(database_models.User).filter(database_models.User.id == token_data.id).first()

    return user
