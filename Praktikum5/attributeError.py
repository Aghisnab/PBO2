class Idol:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

idol1 = Idol("Renjun", 22)

try:
    print(idol1.grup)
except AttributeError:
    print("Objek tidak memiliki atribut yang diminta!")