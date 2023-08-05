CREATE TABLE `tinh_thanh` (
  `id` int PRIMARY KEY,
  `ten` varchar(50) NOT NULL
);

CREATE TABLE `quan_huyen` (
  `id` int PRIMARY KEY,
  `ten` varchar(50) NOT NULL,
  `id_tinh_thanh` int,
  FOREIGN KEY (`id_tinh_thanh`) REFERENCES `tinh_thanh` (`id`)
);

CREATE TABLE `phuong_xa` (
  `id` int PRIMARY KEY,
  `ten` varchar(50) NOT NULL,
  `id_quan_huyen` int,
  FOREIGN KEY (`id_quan_huyen`) REFERENCES `quan_huyen` (`id`)
);

CREATE TABLE `phan_quyen_nguoi_dung` (
  `id` int PRIMARY KEY,
  `phan_quyen` varchar(50) NOT NULL
);

CREATE TABLE `nguoi_dung` (
  `id` int PRIMARY KEY,
  `ho_ten` varchar(20) NOT NULL,
  `sdt` varchar(15) NOT NULL,
  `ngay_sinh` date,
  `email` varchar(50) NOT NULL,
  `mat_khau` varchar(50) NOT NULL,
  `id_phuong_xa` int,
  `dia_chi` varchar(50),
  `id_phan_quyen_nguoi_dung` int,
  `trang_thai` int,
  FOREIGN KEY (`id_phuong_xa`) REFERENCES `phuong_xa` (`id`),
  FOREIGN KEY (`id_phan_quyen_nguoi_dung`) REFERENCES `phan_quyen_nguoi_dung` (`id`)
);

CREATE TABLE `doanh_nghiep` (
  `id` int PRIMARY KEY,
  `id_chu_san` int,
  `ten_doanh_nghiep` varchar(50) NOT NULL,
  `id_phuong_xa` int,
  `dia_chi` text,
  `mo_ta` text,
  `danh_sach_hinh_anh` text,
  `trang_thai` int,
  FOREIGN KEY (`id_phuong_xa`) REFERENCES `phuong_xa` (`id`),
  FOREIGN KEY (`id_chu_san`) REFERENCES `nguoi_dung` (`id`)
);

CREATE TABLE `san_bong` (
  `id` int PRIMARY KEY,
  `id_doanh_nghiep` int,
  `ten_san_bong` varchar(50) NOT NULL,
  `trang_thai` int,
  FOREIGN KEY (`id_doanh_nghiep`) REFERENCES `doanh_nghiep` (`id`)
);

CREATE TABLE `gia_thue_san` (
  `id` int PRIMARY KEY,
  `id_san_bong` int,
  `gio_bat_dau` time NOT NULL,
  `gio_ket_thuc` time NOT NULL,
  `gia_tien` decimal(10, 2) NOT NULL,
  FOREIGN KEY (`id_san_bong`) REFERENCES `san_bong` (`id`)
);

CREATE TABLE `danh_gia` (
  `id_danh_gia` int PRIMARY KEY,
  `id_khach_hang` int,
  `id_doanh_nghiep` int,
  `sao` int,
  `noi_dung` varchar(255),
  FOREIGN KEY (`id_khach_hang`) REFERENCES `nguoi_dung` (`id`),
  FOREIGN KEY (`id_doanh_nghiep`) REFERENCES `doanh_nghiep` (`id`)
);

CREATE TABLE `dat_san` (
  `id` int PRIMARY KEY,
  `id_khach_hang` int,
  `ngay_thue` date,
  `trang_thai` int,
  FOREIGN KEY (`id_khach_hang`) REFERENCES `nguoi_dung` (`id`)
);

CREATE TABLE `chi_tiet_dat_san` (
  `id` int PRIMARY KEY,
  `id_dat_san` int,
  `id_gia_thue_san` int,
  `gia_tien` int,
  FOREIGN KEY (`id_dat_san`) REFERENCES `dat_san` (`id`),
  FOREIGN KEY (`id_gia_thue_san`) REFERENCES `gia_thue_san` (`id`)
);

CREATE TABLE `thanh_toan` (
  `id_thanh_toan` int PRIMARY KEY,
  `id_dat_san` int,
  `gia_tien` DECIMAL(10,2),
  `ngay_thanh_toan` DATETIME,
  FOREIGN KEY (`id_dat_san`) REFERENCES `dat_san` (`id`)
);

INSERT INTO `tinh_thanh` (`id`, `ten`) VALUES
(1, 'Hà Nội'),
(2, 'Hồ Chí Minh'),
(3, 'Đà Nẵng');

INSERT INTO `quan_huyen` (`id`, `ten`, `id_tinh_thanh`) VALUES
(1, 'Quận Ba Đình', 1),
(2, 'Quận Hoàn Kiếm', 1),
(3, 'Quận Tây Hồ', 1),
(4, 'Quận 1', 2),
(5, 'Quận 2', 2),
(6, 'Quận 3', 2),
(7, 'Quận Hải Châu', 3),
(8, 'Quận Thanh Khê', 3),
(9, 'Quận Liên Chiểu', 3);

INSERT INTO `phuong_xa` (`id`, `ten`, `id_quan_huyen`) VALUES
(1, 'Phúc Xá', 1),
(2, 'Ngọc Hà', 1),
(3, 'Yên Phụ', 1),
(4, 'Bến Nghé', 4),
(5, 'Cầu Kho', 4),
(6, 'Cô Giang', 4),
(7, 'Hải Châu 1', 7),
(8, 'Hải Châu 2', 7),
(9, 'Hoà Minh', 9);

INSERT INTO `phan_quyen_nguoi_dung` (`id`, `phan_quyen`) VALUES
(1, 'Quản trị viên'),
(2, 'Người dùng thường');

INSERT INTO `nguoi_dung` (`id`, `ho_ten`, `sdt`, `ngay_sinh`, `email`, `mat_khau`, `id_phuong_xa`, `dia_chi`, `id_phan_quyen_nguoi_dung`, `trang_thai`) VALUES
(1, 'Nguyễn Văn A', '0123456789', '1990-01-01', 'nguyenvana@gmail.com', '123456', 1, 'Số 10, Ngõ 123, Đường ABC', 1, 1);

INSERT INTO `doanh_nghiep` (`id`, `id_chu_san`, `ten_doanh_nghiep`, `id_phuong_xa`, `dia_chi`, `mo_ta`, `danh_sach_hinh_anh`, `trang_thai`) VALUES
(1, 1, 'Sân Bóng Mini Sao', 9, '12 Hoàng Văn Thá', 'Sân bóng đẹp, tiện nghi', '1.jpg;2.jpg;3.jpg', 1),
(2, 1, 'Sân bóng đá mini Trung Nghĩa', 9, '3589+QXV', 'Sân bóng rộng rãi, thoáng mát', '2.jpg;3.jpg', 1),
(3, 1, 'Sân Bóng Liên Chiểu - Nhật Nga', 9, '522 Nguyễn Lương Bằng', 'Sân bóng sạch sẽ, an toàn', '3.jpg', 1);

INSERT INTO `san_bong` (`id`, `id_doanh_nghiep`, `ten_san_bong`, `trang_thai`) VALUES
(1, 1, 'Sân bóng 5 người', 1),
(2, 1, 'Sân bóng 7 người', 1),
(3, 2, 'Sân bóng 11 người', 1);

INSERT INTO `gia_thue_san` (`id`, `id_san_bong`, `gio_bat_dau`, `gio_ket_thuc`, `gia_tien`) VALUES
(1, 1, '08:00:00', '10:00:00', 500000),
(2, 1, '10:00:00', '12:00:00', 600000),
(3, 2, '08:00:00', '10:00:00', 700000),
(4, 2, '10:00:00', '12:00:00', 800000),
(5, 3, '08:00:00', '10:00:00', 900000),
(6, 3, '10:00:00', '12:00:00', 1000000);

INSERT INTO `danh_gia` (`id_danh_gia`, `id_khach_hang`, `id_doanh_nghiep`, `sao`, `noi_dung`) VALUES
(1, 1, 1, 3, 'Sân bóng đẹp, nhân viên nhiệt tình');


INSERT INTO `dat_san` (`id`, `id_khach_hang`, `ngay_thue`, `trang_thai`) VALUES
(1, 1, '2023-07-28', 1);

INSERT INTO `chi_tiet_dat_san` (`id`, `id_dat_san`, `id_gia_thue_san`, `gia_tien`) VALUES
(1, 1, 1, 500000),
(2, 1, 2, 600000);


INSERT INTO `thanh_toan` (`id_thanh_toan`, `id_dat_san`, `gia_tien`, `ngay_thanh_toan`) VALUES
(1, 1, 1100000, '2023-07-28 10:00:00'),
(2, 1, 1500000, '2023-07-29 09:00:00'),
(3, 1, 1900000, '2023-07-30 08:00:00');