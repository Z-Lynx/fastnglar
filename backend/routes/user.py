# app/routes/user.py

from fastapi import APIRouter, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session
from models.models import NguoiDung
from schemas.user import User as UserSchema,  UserCreate, UserUpdate
from database.session import get_db
from fastapi import APIRouter, Depends, HTTPException
from models import models
from schemas import doanhnghiep as schemas
import os
from fastapi import File, UploadFile
from typing import List


router = APIRouter()

@router.post("/doanh_nghiep/", response_model=schemas.DoanhNghiep)
def create_doanh_nghiep(
    doanh_nghiep: schemas.DoanhNghiepCreate,
    images: List[UploadFile] = File(default=[]),
    db: Session = Depends(get_db)
):
    # Process and save the images
    image_filenames = []
    for image in images:
        filename = f"media/image/{image.filename}"
        with open(filename, "wb") as f:
            f.write(image.file.read())
        image_filenames.append(filename)
    
    # Join the image filenames with ";"
    last_id = db.query(func.max(models.DoanhNghiep.id)).scalar() or 0
    new_id = last_id + 1
    doanh_nghiep.id_chu_san = 1
    doanh_nghiep.danh_sach_hinh_anh = ";".join(image_filenames)
    print(db_doanh_nghiep)
    # Create the DoanhNghiep object and save it to the database
    db_doanh_nghiep = models.DoanhNghiep(**doanh_nghiep.dict())
    db.add(db_doanh_nghiep)
    db.commit()
    db.refresh(db_doanh_nghiep)
    return db_doanh_nghiep



@router.get("/doanh_nghiep/{doanh_nghiep_id}", response_model=schemas.DoanhNghiep)
def read_doanh_nghiep(doanh_nghiep_id: int, db: Session = Depends(get_db)):
    doanh_nghiep = db.query(models.DoanhNghiep).filter(models.DoanhNghiep.id == doanh_nghiep_id).first()
    if not doanh_nghiep:
        raise HTTPException(status_code=404, detail="DoanhNghiep not found")
    return doanh_nghiep


@router.put("/doanh_nghiep/{doanh_nghiep_id}", response_model=schemas.DoanhNghiep)
def update_doanh_nghiep(
    doanh_nghiep_id: int,
    doanh_nghiep: schemas.DoanhNghiepUpdate,
    images: List[UploadFile] = File(default=[]),
    db: Session = Depends(get_db)
):
    db_doanh_nghiep = db.query(models.DoanhNghiep).filter(models.DoanhNghiep.id == doanh_nghiep_id).first()
    if not db_doanh_nghiep:
        raise HTTPException(status_code=404, detail="DoanhNghiep not found")
    
    # Update the simple fields from the request
    for key, value in doanh_nghiep.dict().items():
        setattr(db_doanh_nghiep, key, value)
    
    # Process and save the images
    image_filenames = []
    for image in images:
        filename = f"media/image/{image.filename}"
        with open(filename, "wb") as f:
            f.write(image.file.read())
        image_filenames.append(filename)
    
    # Join the image filenames with ";"
    db_doanh_nghiep.danh_sach_hinh_anh = ";".join(image_filenames)
    
    db.commit()
    db.refresh(db_doanh_nghiep)
    return db_doanh_nghiep



@router.delete("/doanh_nghiep/{doanh_nghiep_id}", response_model=schemas.DoanhNghiep)
def delete_doanh_nghiep(doanh_nghiep_id: int, db: Session = Depends(get_db)):
    doanh_nghiep = db.query(models.DoanhNghiep).filter(models.DoanhNghiep.id == doanh_nghiep_id).first()
    if not doanh_nghiep:
        raise HTTPException(status_code=404, detail="DoanhNghiep not found")
    db.delete(doanh_nghiep)
    db.commit()
    return doanh_nghiep
