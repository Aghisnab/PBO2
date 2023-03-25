print('\nHybrid Inheritance_Kampus\n\n')

class Univ:
    def __init__(self):
        self.univ = 'UMC'
    
    def display(self):
        print('Universitas\t: ',self.univ)

class Fakultas(Univ):
    def __init__(self):
        Univ.__init__(self)
        self.fakultas = 'Teknik'

    def display(self):
        Univ.display(self)
        print('Fakultas\t: ', self.fakultas)

class Prodi(Univ):
    def __init__(self):
        Univ.__init__(self)
        self.prodi = 'Teknik Informatika\n'

    def display(self):
        print('Program Studi\t: ', self.prodi)

class Mhs(Fakultas, Prodi):
    def __init__(self):
        self.name = 'Aghisna Baihaqi'
        Fakultas.__init__(self)
        Prodi.__init__(self)

    def display(self):
        print('Nama\t\t: ', self.name)
        Fakultas.display(self)
        Prodi.display(self)

mhs1 = Mhs()
mhs1.display()
