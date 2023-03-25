print('\nMultiple Inheritance_FILM\n')

class Film:
    def __init__(self,judul,tahun,asal):
        self.judul = judul
        self.tahun = tahun
        self.asal = asal

    def display(self):
        print('Judul\t\t: ',self.judul)
        print('Tahun\t\t: ',self.tahun)
        print('Produksi\t: ',self.asal)


class Jenis:
    def __init__(self,jenis,genre):
        self.jenis = jenis
        self.genre = genre

    def display(self):
        print('Jenis\t\t: ',self.jenis)
        print('Genre\t\t: ',self.genre)

class FilmDetail(Film,Jenis):
    def __init__(self,judul,tahun,asal,jenis,genre):
        Film.__init__(self,judul,tahun,asal)
        Jenis.__init__(self,jenis,genre)

    def display(self):
        super().display()
        print('Jenis\t\t: ',self.jenis)
        print('Genre\t\t: ',self.genre)

film1 = FilmDetail("Heavenly Idol",2023,"Korea Selatan","Drama","Fantasi and Romance Comedy\n")
film1.display()

film2 = FilmDetail("The Glory",2023,"Korea Selatan","Drama","Revenge Tragedy\n")
film2.display()