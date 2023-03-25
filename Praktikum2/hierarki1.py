print('\nHierarchical Inheritance_KPOP\n\n')

class Grup:
    def __init__(self, grup, anggota):
        self.grup = grup
        self.anggota = anggota

    def ket(self):
        print(f'{self.grup} beranggotakan {self.anggota} orang\n\n')
    
    def getGrup(self):
        return self.grup
    
    def getAnggota(self):
        return self.anggota

class Gen(Grup):
    def __init__(self, grup, anggota, gen):
        super().__init__(grup, anggota)
        self.gen = gen
    
    def detail(self):
        print(f'Grup {self.grup} merupakan Generasi Ke-{self.gen} Kpop\n')

    def getGen(self):
        return self.gen

class Agensi(Gen):
    def __init__(self, grup, anggota, gen, fandom, agensi):
        super().__init__(grup, anggota, gen)
        self.fandom = fandom
        self.agensi = agensi

    def keterangan(self):
        print(f'Grup: {self.grup}\nAnggota: {self.anggota} Orang\nFandom: {self.fandom}\nGen: {self.gen}\nAgensi: {self.agensi}\n')

if __name__ == '__main__':
    grup1 = Agensi('EXO',9,3,'EXO-L','SMENT')
    grup1.keterangan()
    grup1.detail()
    grup1.ket()

    grup2 = Agensi('NewJeans',5,4,'Bunnies','HYBE')
    grup2.keterangan()

    grup3 = Agensi('NCT',23,4,'NCT-ZEN','SMENT')
    grup3.keterangan()



