from pydantic import BaseModel
from typing import List 

class DoanhNghiepBase(BaseModel):
    id:int
    id_chu_san: int
    ten_doanh_nghiep: str
    id_phuong_xa: int
    dia_chi: str
    mo_ta: str
    danh_sach_hinh_anh: str
    trang_thai: int

    class Config:
        orm_mode = True


class DoanhNghiepCreate(DoanhNghiepBase):
    pass


class DoanhNghiepUpdate(DoanhNghiepBase):
    pass


class DoanhNghiep(DoanhNghiepBase):
    id: int

    class Config:
        orm_mode = True