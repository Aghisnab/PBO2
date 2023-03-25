print('\nHierarchical Inheritance_Mahasiswa\n\n')

class Mahasiswa:
    def __init__(self, name, nim):
        self.name = name
        self.nim = nim

    def ket(self):
        print(f'{self.name} adalah Mahasiswa UMC dengan NIM {self.nim}\n')
    
    def getName(self):
        return self.name 
    
    def getNim(self):
        return self.nim

class Fakultas(Mahasiswa):
    def __init__(self, name, nim, fakultas):
        super().__init__(name, nim)
        self.fakultas = fakultas
    
    def detail(self):
        print(f'Nama: {self.name}\nNim: {self.nim}\nFakultas: {self.fakultas}\n')

    def getFakultas(self):
        return self.fakultas

class Prodi(Fakultas):
    def __init__(self, name, nim, fakultas, prodi):
        super().__init__(name, nim, fakultas)
        self.prodi = prodi

    def keterangan(self):
        print(f'Nama: {self.name}\nNim: {self.nim}\nFakultas: {self.fakultas}\nProdi: {self.prodi}\n')

if __name__ == '__main__':
    mhs1 = Prodi('Aghisna Baihaqi', 210511034,'Teknik', 'Teknik Informatika')
    mhs1.keterangan()
    mhs1.detail()
    mhs1.ket()
