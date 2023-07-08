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
-- Struktur dari tabel `idol`
--

CREATE TABLE `idol` (
  `idol_debut` char(15) NOT NULL,
  `nama` varchar(150) DEFAULT NULL,
  `jk` enum('L','P') NOT NULL DEFAULT 'L',
  `nama_grup` varchar(50) DEFAULT NULL,
  `Posisi` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `idol`
--

INSERT INTO `idol` (`idol_debut`, `nama`, `jk`, `nama_grup`, `Posisi`) VALUES
('ae2-27102020', 'Winter', 'P', 'Aespa', 'Visual'),
('e4-30102020', 'Sunghoon', 'L', 'Enhypen', 'Visual'),
('ts1-782020', 'Haruto', 'L', 'Treasure', 'Main Rapper');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `idol`
--
ALTER TABLE `idol`
  ADD PRIMARY KEY (`idol_debut`),
  ADD UNIQUE KEY `idol_debut` (`idol_debut`),
  ADD KEY `nama_grup` (`nama_grup`);

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `idol`
--
ALTER TABLE `idol`
  ADD CONSTRAINT `idol_ibfk_1` FOREIGN KEY (`nama_grup`) REFERENCES `grup` (`nama_grup`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
