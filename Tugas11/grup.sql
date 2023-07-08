-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 11 Jun 2023 pada 06.00
-- Versi server: 10.4.25-MariaDB
-- Versi PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbapi_tugas`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `grup`
--

CREATE TABLE `grup` (
  `grup_debut` char(15) NOT NULL,
  `nama_grup` varchar(50) DEFAULT NULL,
  `gender` enum('Boygroup','Girlgroup') NOT NULL DEFAULT 'Boygroup',
  `fandom` varchar(100) DEFAULT NULL,
  `agensi` varchar(50) DEFAULT NULL,
  `member` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `grup`
--

INSERT INTO `grup` (`grup_debut`, `nama_grup`, `gender`, `fandom`, `agensi`, `member`) VALUES
('HB-30112020', 'Enhypen', 'Boygroup', 'ENGENE', 'Belift Lab', 7),
('SM-17112020', 'Aespa', 'Girlgroup', 'MY', 'SM Ent', 4),
('YG-7082020', 'Treasure', 'Boygroup', 'Treasure Maker', 'YG Ent', 10);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `grup`
--
ALTER TABLE `grup`
  ADD PRIMARY KEY (`grup_debut`),
  ADD UNIQUE KEY `grup_debut` (`grup_debut`),
  ADD KEY `nama_grup` (`nama_grup`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
