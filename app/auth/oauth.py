from jose import JWTError, jwt
from datetime import datetime, timedelta
# from ..schemas import user_models
from ..db import database, database_models
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from ..environment_config import settings