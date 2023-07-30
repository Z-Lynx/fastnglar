# app/schemas/user.py

from typing import Optional
from datetime import date
from pydantic import BaseModel

class UserBase(BaseModel):
    ho_ten: str
    sdt: str
    ngay_sinh: date
    email: str
    dia_chi: str
    id_phuong_xa: int

class UserCreate(UserBase):
    ho_ten: str
    sdt: str
    ngay_sinh: date
    email: str
    dia_chi: str
    id_phuong_xa: int
    mat_khau: str
    id_phan_quyen_nguoi_dung: int

class UserUpdate(UserBase):
    mat_khau: Optional[str] = None
    id_phuong_xa: Optional[int] = None

class User(UserBase):
    id: int
    id_phuong_xa: int

