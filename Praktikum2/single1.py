print('\nSingle Inheritance_SEBLAK\n\n')

class Menu:
    def __init__(self,menu,level):
        self.menu = menu
        self.level = level

    def info(self):
        print('Menu\t\t: ',self.menu)
        print('Level\t\t: ',self.level)

class Pesan(Menu):
    def __init__(self,menu,level,topping,tambahan):
        super().__init__(menu,level)
        self.topping = topping
        self.tambahan = tambahan
       
    def pesan(self):
        print('Topping\t\t: ',self.topping)
        print('Tambahan\t: ',self.tambahan)

pesan1 = Pesan("Seblak",4,"Batagor dan Seafood","Tidak pake kol\n")
pesan1.info()
pesan1.pesan()


pesan2 = Pesan("Mie Get","Pedas Banget","Seafood","-\n")
pesan2.info()
pesan2.pesan()

