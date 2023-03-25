print('\nSingle Inheritance_DATA\n\n')

class diri:
    def __init__(self):
        self.nama = "Aghisna Baihaqi"
        self.umur = 20
    
    def info(self):
        print('Nama\t\t: ',self.nama)
        print(f'Umur\t\t:  {self.umur} Tahun')

class data(diri):
    def __init__(self):
        super().__init__()
        self.status = "Mahasiswa"
        self.univ = "Universitas Muhammadiyah Cirebon"
        self.prodi = "Teknik Informatika"
        self.alamat = "Subang\n"

    def display(self):
        print('Status\t\t: ',self.status)
        print('Universitas\t: ',self.univ)
        print('Jurusan\t\t: ',self.prodi)
        print('Alamat\t\t: ',self.alamat)

a = data()
a.info()
a.display()