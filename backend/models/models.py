# coding: utf-8
from sqlalchemy import Column, DECIMAL, Date, DateTime, ForeignKey, Integer, String, Text, Time
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class PhanQuyenNguoiDung(Base):
    __tablename__ = 'phan_quyen_nguoi_dung'

    id = Column(Integer, primary_key=True)
    phan_quyen = Column(String(50), nullable=False)


class TinhThanh(Base):
    __tablename__ = 'tinh_thanh'

    id = Column(Integer, primary_key=True)
    ten = Column(String(50), nullable=False)


class QuanHuyen(Base):
    __tablename__ = 'quan_huyen'

    id = Column(Integer, primary_key=True)
    ten = Column(String(50), nullable=False)
    id_tinh_thanh = Column(ForeignKey('tinh_thanh.id'))

    tinh_thanh = relationship('TinhThanh')


class PhuongXa(Base):
    __tablename__ = 'phuong_xa'

    id = Column(Integer, primary_key=True)
    ten = Column(String(50), nullable=False)
    id_quan_huyen = Column(ForeignKey('quan_huyen.id'))

    quan_huyen = relationship('QuanHuyen')


class NguoiDung(Base):
    __tablename__ = 'nguoi_dung'

    id = Column(Integer, primary_key=True)
    ho_ten = Column(String(20), nullable=False)
    sdt = Column(String(15), nullable=False)
    ngay_sinh = Column(Date)
    email = Column(String(50), nullable=False)
    mat_khau = Column(String(50), nullable=False)
    id_phuong_xa = Column(ForeignKey('phuong_xa.id'))
    dia_chi = Column(String(50))
    id_phan_quyen_nguoi_dung = Column(ForeignKey('phan_quyen_nguoi_dung.id'))
    trang_thai = Column(Integer)

    phan_quyen_nguoi_dung = relationship('PhanQuyenNguoiDung')
    phuong_xa = relationship('PhuongXa')


class DatSan(Base):
    __tablename__ = 'dat_san'

    id = Column(Integer, primary_key=True)
    id_khach_hang = Column(ForeignKey('nguoi_dung.id'))
    ngay_thue = Column(Date)
    trang_thai = Column(Integer)

    nguoi_dung = relationship('NguoiDung')


class DoanhNghiep(Base):
    __tablename__ = 'doanh_nghiep'

    id = Column(Integer, primary_key=True)
    id_chu_san = Column(ForeignKey('nguoi_dung.id'))
    ten_doanh_nghiep = Column(String(50), nullable=False)
    id_phuong_xa = Column(ForeignKey('phuong_xa.id'))
    dia_chi = Column(Text)
    mo_ta = Column(Text)
    danh_sach_hinh_anh = Column(Text)
    trang_thai = Column(Integer)

    nguoi_dung = relationship('NguoiDung')
    phuong_xa = relationship('PhuongXa')


class DanhGia(Base):
    __tablename__ = 'danh_gia'

    id_danh_gia = Column(Integer, primary_key=True)
    id_khach_hang = Column(ForeignKey('nguoi_dung.id'))
    id_doanh_nghiep = Column(ForeignKey('doanh_nghiep.id'))
    sao = Column(Integer)
    noi_dung = Column(String(255))

    doanh_nghiep = relationship('DoanhNghiep')
    nguoi_dung = relationship('NguoiDung')


class SanBong(Base):
    __tablename__ = 'san_bong'

    id = Column(Integer, primary_key=True)
    id_doanh_nghiep = Column(ForeignKey('doanh_nghiep.id'))
    ten_san_bong = Column(String(50), nullable=False)
    trang_thai = Column(Integer)

    doanh_nghiep = relationship('DoanhNghiep')


class ThanhToan(Base):
    __tablename__ = 'thanh_toan'

    id_thanh_toan = Column(Integer, primary_key=True)
    id_dat_san = Column(ForeignKey('dat_san.id'))
    gia_tien = Column(DECIMAL(10, 2))
    ngay_thanh_toan = Column(DateTime)

    dat_san = relationship('DatSan')


class GiaThueSan(Base):
    __tablename__ = 'gia_thue_san'

    id = Column(Integer, primary_key=True)
    id_san_bong = Column(ForeignKey('san_bong.id'))
    gio_bat_dau = Column(Time, nullable=False)
    gio_ket_thuc = Column(Time, nullable=False)
    gia_tien = Column(DECIMAL(10, 2), nullable=False)

    san_bong = relationship('SanBong')


class ChiTietDatSan(Base):
    __tablename__ = 'chi_tiet_dat_san'

    id = Column(Integer, primary_key=True)
    id_dat_san = Column(ForeignKey('dat_san.id'))
    id_gia_thue_san = Column(ForeignKey('gia_thue_san.id'))
    gia_tien = Column(Integer)

    dat_san = relationship('DatSan')
    gia_thue_san = relationship('GiaThueSan')
