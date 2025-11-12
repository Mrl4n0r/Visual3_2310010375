-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 12 Nov 2025 pada 08.36
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `visual3_2310010375`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `absensi`
--

CREATE TABLE `absensi` (
  `kd_absen` int(11) NOT NULL,
  `nik` varchar(20) NOT NULL,
  `nama_karyawan` varchar(100) NOT NULL,
  `tgl_rekap` date NOT NULL,
  `status_kehadiran` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `absensi`
--

INSERT INTO `absensi` (`kd_absen`, `nik`, `nama_karyawan`, `tgl_rekap`, `status_kehadiran`) VALUES
(123, '2310010375', 'Muhammad Maulana', '2025-10-29', 'Izin'),
(1213, '2456', 'adul', '2025-10-29', 'Izin'),
(3333, '32123', 'qsas', '2025-10-30', 'Hadir'),
(4445, '1210', 'adtu', '2025-11-12', 'Izin');

-- --------------------------------------------------------

--
-- Struktur dari tabel `gaji`
--

CREATE TABLE `gaji` (
  `kd_gaji` int(11) NOT NULL,
  `nik` varchar(20) NOT NULL,
  `tunjangan` decimal(12,0) DEFAULT 0,
  `total_lembur` decimal(12,0) DEFAULT 0,
  `total_gaji` decimal(12,0) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `gaji`
--

INSERT INTO `gaji` (`kd_gaji`, `nik`, `tunjangan`, `total_lembur`, `total_gaji`) VALUES
(43253, '2310010375', 5000000, 0, 10000000),
(43254, '2310010199', 1000000, 2, 2000000);

-- --------------------------------------------------------

--
-- Struktur dari tabel `jabatan`
--

CREATE TABLE `jabatan` (
  `kd_jabatan` char(20) NOT NULL,
  `nama_jabatan` varchar(50) NOT NULL,
  `tunjangan` int(11) DEFAULT NULL,
  `gaji_pokok` decimal(10,2) NOT NULL,
  `deskripsi` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `jabatan`
--

INSERT INTO `jabatan` (`kd_jabatan`, `nama_jabatan`, `tunjangan`, `gaji_pokok`, `deskripsi`) VALUES
('001', 'CEO', 5000000, 7000000.00, 'Oke'),
('002', 'Karyawan', 1000000, 2000000.00, 'Mantap');

-- --------------------------------------------------------

--
-- Struktur dari tabel `karyawan`
--

CREATE TABLE `karyawan` (
  `nik` varchar(20) NOT NULL,
  `nama_karyawan` varchar(100) NOT NULL,
  `jk` enum('Laki-laki','Perempuan') NOT NULL,
  `tgl_lahir` date DEFAULT NULL,
  `alamat_karyawan` text DEFAULT NULL,
  `agama` enum('Islam','Kristen','Katolik','Hindu','Buddha','Khonghucu') DEFAULT NULL,
  `no_hp` varchar(20) DEFAULT NULL,
  `pendidikan` varchar(50) DEFAULT NULL,
  `kd_jabatan` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `karyawan`
--

INSERT INTO `karyawan` (`nik`, `nama_karyawan`, `jk`, `tgl_lahir`, `alamat_karyawan`, `agama`, `no_hp`, `pendidikan`, `kd_jabatan`) VALUES
('2310010199', 'Husnul Khatimah', 'Perempuan', '2005-11-04', 'haruyan', 'Islam', '082637284611', 'SMA 1 Barabai', '003'),
('2310010375', 'Muhammad Maulana', 'Laki-laki', '2005-08-05', 'Barabai', 'Islam', '087762544115', 'MA Muhajirin', '001');

-- --------------------------------------------------------

--
-- Struktur dari tabel `mitra`
--

CREATE TABLE `mitra` (
  `kd_mitra` varchar(20) NOT NULL,
  `nama_mitra` varchar(100) NOT NULL,
  `alamat_mitra` text DEFAULT NULL,
  `telepon_mitra` varchar(20) DEFAULT NULL,
  `email_mitra` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `mitra`
--

INSERT INTO `mitra` (`kd_mitra`, `nama_mitra`, `alamat_mitra`, `telepon_mitra`, `email_mitra`) VALUES
('001', 'Ayam Gepeng', 'Banjar', '082127647821', 'aymgpeng22@gmail.com'),
('002', 'Bebek gepeng', 'barabai', '089735467890', 'bebekgepeng666@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `absensi`
--
ALTER TABLE `absensi`
  ADD PRIMARY KEY (`kd_absen`);

--
-- Indeks untuk tabel `gaji`
--
ALTER TABLE `gaji`
  ADD PRIMARY KEY (`kd_gaji`);

--
-- Indeks untuk tabel `jabatan`
--
ALTER TABLE `jabatan`
  ADD PRIMARY KEY (`kd_jabatan`);

--
-- Indeks untuk tabel `karyawan`
--
ALTER TABLE `karyawan`
  ADD PRIMARY KEY (`nik`);

--
-- Indeks untuk tabel `mitra`
--
ALTER TABLE `mitra`
  ADD PRIMARY KEY (`kd_mitra`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `absensi`
--
ALTER TABLE `absensi`
  MODIFY `kd_absen` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4450;

--
-- AUTO_INCREMENT untuk tabel `gaji`
--
ALTER TABLE `gaji`
  MODIFY `kd_gaji` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43263;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
