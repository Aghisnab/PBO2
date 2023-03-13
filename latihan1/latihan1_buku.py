class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
    def info(self):
        print(f"Judul: {self.judul}\nPenulis: {self.penulis} \n")
bukuA = Buku("Romeo And Juliet", "William Shakespeare")
bukuA.info()
