# app/routes/user.py

from fastapi import APIRouter, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session
from models.models import NguoiDung
from schemas.user import User as UserSchema,  UserCreate, UserUpdate
from database.session import get_db

router = APIRouter()


@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(NguoiDung).all()
    return users

@router.post("/users")
async def create_user(userReq: UserCreate, db: Session = Depends(get_db)):
    last_id = db.query(func.max(NguoiDung.id)).scalar() or 0
    new_id = last_id + 1
    db_user = NguoiDung(
        id = new_id,
        ho_ten=userReq.ho_ten,
        sdt=userReq.sdt,
        ngay_sinh=userReq.ngay_sinh,
        email=userReq.email,
        mat_khau=userReq.mat_khau,
        id_phuong_xa=userReq.id_phuong_xa,
        dia_chi=userReq.dia_chi,
        id_phan_quyen_nguoi_dung=userReq.id_phan_quyen_nguoi_dung,
        trang_thai=1
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# @router.put("/users/{user_id}", response_model=User)
# async def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)) -> Any:
#     db_user = db.query(User).filter(User.id == user_id).first()
#     if not db_user:
#         raise HTTPException(status_code=404, detail="User not found")
#     for field, value in user.dict(exclude_unset=True).items():
#         setattr(db_user, field, value)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

# @router.get("/users/{user_id}", response_model=User)
# async def get_user(user_id: int, db: Session = Depends(get_db)) -> Any:
#     db_user = db.query(User).filter(User.id == user_id).first()
#     if not db_user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user