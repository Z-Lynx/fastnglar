# app/routes/user.py

from fastapi import APIRouter, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session
from models.models import NguoiDung
from schemas.user import User as UserSchema,  UserCreate, UserUpdate
from database.session import get_db

router = APIRouter()
