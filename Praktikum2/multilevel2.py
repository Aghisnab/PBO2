print('\nMultilevel Inheritance_ALAMAT\n')

class Negara:
    def __init__(self):
        self.negara = 'Indonesia'

    def display(self):
        print('Negara\t\t: ',self.negara)

class Provinsi(Negara):
    def __init__(self):
        Negara.__init__(self)
        self.provinsi = 'Jawa Barat'

    def display(self):
        Negara().display()
        print('Provinsi\t: ',self.provinsi)

class Kota(Provinsi):
    def __init__(self):
        Provinsi.__init__(self)
        self.kota = 'Subang'

    def display(self):
        Provinsi().display()
        print('Kota\t\t: ',self.kota)

class Kecamatan(Kota):
    def __init__(self):
        Kota.__init__(self)
        self.kecamatan = 'Purwadadi\n'

    def display(self):
        Kota().display()
        print('Kecamatan\t: ',self.kecamatan)

alamat = Kecamatan()
alamat.display()