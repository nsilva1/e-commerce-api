from fastapi import status, HTTPException, Depends, APIRouter, Response
from sqlalchemy.orm import Session
from ..db.database import get_db
from ..db.database_models import User
from ..schemas.user_schemas import UserDetails, BaseUser, UpdateUser
from ..auth.hash import verify_password, hash_password
from ..auth.oauth import create_access_token, get_current_user
from ..utils.enums import AccessCode, Roles

router = APIRouter(
    prefix='/user',
    tags=['Users']
)


# get a user by id
@router.get("/{id}", response_model=UserDetails)
def get_user(id: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    user = db.query(User).filter(User.id == id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    return user


# get all users
@router.get("/", response_model=list[UserDetails])
def get_all_users(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):

    users = db.query(User).all()

    return users


# update a user
@router.put("/{id}/{authorizationCode}", response_model=UserDetails)
def update_user(id: str, authorizationCode: str, user: UpdateUser, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):

    db_user = db.query(User).filter(User.id == id).first()

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    if current_user.role not in (Roles.admin, Roles.super_admin):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Action Forbidden")

    if user.role in (Roles.super_admin, Roles.admin) and authorizationCode not in (AccessCode.super_admin, AccessCode.admin):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Authorization Code")

    if user.password:
        hashed_password = hash_password(user.password)
        user.password = hashed_password

    for var, value in user:
        setattr(db_user, var, value)

    db.commit()
    db.refresh(db_user)

    return db_user


# delete a user
@router.delete("/{id}/{authorizationCode}")
def delete_user(id: str, authorizationCode: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_user = db.query(User).filter(User.id == id).first()

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    if current_user.role not in (Roles.admin, Roles.super_admin):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Action Forbidden")

    if db_user.role in (Roles.admin) and authorizationCode not in (AccessCode.super_admin, AccessCode.admin):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Authorization Code")
    
    if db_user.role in (Roles.super_admin) and authorizationCode not in (AccessCode.super_admin):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Authorization Code")

    db.delete(db_user)
    db.commit()

    return {"message": "User deleted successfully"}