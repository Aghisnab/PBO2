print('\nMultiple Inheritance_NCT\n')

class NCT:
    def __init__(self, nama, asal):
        self.nama = nama
        self.asal = asal
    def display_info(self):
        print(f"Nama: {self.nama}")
        print(f"Asal: {self.asal}")

class Dream:
    def __init__(self, posisi, line):
        self.posisi = posisi
        self.line = line
    def display_info(self):
        print(f"Posisi: {self.posisi}")
        print(f"Line: {self.line}")

class Ilichil:
    def __init__(self, posisi1, line1):
        self.posisi1 = posisi1
        self.line1 = line1
    def display_info(self):
        print(f"Posisi: {self.posisi1}")
        print(f"Line: {self.line1}")

class Universe(Dream, Ilichil):
    def __init__(self, nama, asal, posisi, line, posisi1, line1):
        NCT.__init__(self, nama, asal)
        Dream.__init__(self, posisi, line)
        Ilichil.__init__(self, posisi1, line1)
    def display1(self):
        super().display_info()
        print(f"Nama: {self.nama}")
        print(f"Asal: {self.asal}")
        print(f"Posisi: {self.posisi}")
        print(f"Line: {self.line}")
    def display1(self):
        print(f"Nama: {self.nama}")
        print(f"Asal: {self.asal}")
        print(f"Posisi: {self.posisi1}")
        print(f"Line: {self.line1}")

nct1 = Universe("Renjun","China","Lead Vocal", "2000",'Lead Vocal','2000\n')
nct1.display1()       

nct2 = Universe("Jaemin","Korea","Center and Visual", "2001",'Visual and Center','2001\n')
nct2.display1()       