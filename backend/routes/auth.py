# app/routes/NguoiDung.py

from fastapi import APIRouter, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session
from models.models import NguoiDung
from schemas.auth import Token, authenticate_user
from schemas.user import  UserCreate, UserUpdate
from database.session import get_db
from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from jose import JWTError, jwt
import bcrypt
from utils.auth import create_access_token, get_current_user

router = APIRouter()

ACCESS_TOKEN_EXPIRE_MINUTES = 30
@router.post("/register", response_model=Token)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    # Get NguoiDung registration data from the user_data parameter
    email = user_data.email
    password = user_data.mat_khau

    # Check if the username or email already exists in the database
    nguoi_dung_by_email = db.query(NguoiDung).filter(NguoiDung.email == email).first()
    if nguoi_dung_by_email:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Create a new NguoiDung in the database
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    last_id = db.query(func.max(NguoiDung.id)).scalar() or 0
    new_id = last_id + 1
    new_user = NguoiDung(
        id= new_id,
        email=email,
        mat_khau=hashed_password,
        ho_ten=user_data.ho_ten,
        sdt=user_data.sdt,
        ngay_sinh=user_data.ngay_sinh,
        id_phuong_xa=user_data.id_phuong_xa,
        dia_chi=user_data.dia_chi,
        id_phan_quyen_nguoi_dung=user_data.id_phan_quyen_nguoi_dung,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Create a JWT for the NguoiDung
    payload = {"id": new_id, "email": email}
    jwt_token = jwt.encode(payload, "mysecretkey", algorithm="HS256")

    # Return the JWT
    return {"access_token": jwt_token, "token_type": "bearer"}

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Get NguoiDung login data from the form
    username = form_data.username
    password = form_data.password

    # Check if the username exists in the database
    NguoiDung = db.query(NguoiDung).filter(NguoiDung.username == username).first()
    if not NguoiDung:
        raise HTTPException(status_code=400, detail="Invalid username or password")

    # Check if the password is correct
    if not bcrypt.checkpw(password.encode("utf-8"), NguoiDung.password):
        raise HTTPException(status_code=400, detail="Invalid username or password")

    # Create a JWT for the NguoiDung
    payload = {"username": username, "email": NguoiDung.email}
    jwt_token = jwt.encode(payload, "mysecretkey", algorithm="HS256")

    # Return the JWT
    return {"access_token": jwt_token, "token_type": "bearer"}

@router.get("/users/me")
def read_users_me(current_user: str = Depends(get_current_user)):
    return {"username": current_user}

@router.post("/token", response_model=Token)  # Use the Token model as the response model
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    NguoiDung = authenticate_user(db, form_data.username, form_data.password)
    if not NguoiDung:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": NguoiDung.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
