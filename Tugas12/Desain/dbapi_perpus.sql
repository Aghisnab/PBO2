CREATE TABLE `anggota` (
	`idAnggota` INT NOT NULL AUTO_INCREMENT,
	`kodeAnggota` INT NOT NULL UNIQUE,
	`nama` varchar(50) NOT NULL,
	`alamat` varchar(100) NOT NULL,
	`bergabung` DATE NOT NULL,
	PRIMARY KEY (`idAnggota`)
);

CREATE TABLE `buku` (
	`idBuku` INT NOT NULL AUTO_INCREMENT,
	`kodeBuku` varchar(11) NOT NULL UNIQUE,
	`judul` varchar(100) NOT NULL,
	`kodeKategori` varchar(11) NOT NULL,
	`penulis` varchar(50) NOT NULL,
	`penerbit` varchar(50) NOT NULL,
	`tahun` INT NOT NULL,
	PRIMARY KEY (`idBuku`)
);

CREATE TABLE `kategori` (
	`idKategori` INT NOT NULL AUTO_INCREMENT,
	`kodeKategori` varchar(11) NOT NULL UNIQUE,
	`namaKategori` varchar(50) NOT NULL,
	PRIMARY KEY (`idKategori`)
);

CREATE TABLE `pinjam` (
	`idPinjam` INT NOT NULL AUTO_INCREMENT,
	`kodePinjam` varchar(11) NOT NULL,
	`kodeAnggota` INT NOT NULL,
	`kodeBuku` varchar(11) NOT NULL,
	`tglKembali` DATE NOT NULL,
	PRIMARY KEY (`idPinjam`)
);

CREATE TABLE `kembali` (
	`idKembali` INT NOT NULL AUTO_INCREMENT,
	`kodeKembali` varchar(11) NOT NULL UNIQUE,
	`kodeAnggota` INT NOT NULL,
	`kodePinjam` varchar(11) NOT NULL,
	`kodeBuku` varchar(11) NOT NULL,
	`tglDikembalikan` DATE NOT NULL,
	`denda` INT,
	PRIMARY KEY (`idKembali`)
);

ALTER TABLE `buku` ADD CONSTRAINT `buku_fk0` FOREIGN KEY (`kodeKategori`) REFERENCES `kategori`(`kodeKategori`);

ALTER TABLE `pinjam` ADD CONSTRAINT `pinjam_fk0` FOREIGN KEY (`kodeAnggota`) REFERENCES `anggota`(`kodeAnggota`);

ALTER TABLE `pinjam` ADD CONSTRAINT `pinjam_fk1` FOREIGN KEY (`kodeBuku`) REFERENCES `buku`(`kodeBuku`);

ALTER TABLE `kembali` ADD CONSTRAINT `kembali_fk0` FOREIGN KEY (`kodeAnggota`) REFERENCES `anggota`(`kodeAnggota`);

ALTER TABLE `kembali` ADD CONSTRAINT `kembali_fk1` FOREIGN KEY (`kodePinjam`) REFERENCES `pinjam`(`kodePinjam`);

ALTER TABLE `kembali` ADD CONSTRAINT `kembali_fk2` FOREIGN KEY (`kodeBuku`) REFERENCES `buku`(`kodeBuku`);






