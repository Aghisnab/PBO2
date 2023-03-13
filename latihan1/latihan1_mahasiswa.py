class Mahasiswa:
    def __init__(self, nama, npm):
        self.nama = nama
        self.npm = npm
    def info(self):
        print(f"Nama: {self.nama}\nNIM: {self.npm} \n")
mahasiswaB = Mahasiswa("Aghisna Baihaqi", "210511034")
mahasiswaB.info()