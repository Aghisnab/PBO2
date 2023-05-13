print("\nAghisna Baihaiqi\n210511034\nR1\n")

class TabungMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
       
        def luaspermukaan(cls, jari, tinggi):
            return 2 * 22/7 * jari * (jari + tinggi)
        cls.luaspermukaan = classmethod(luaspermukaan)

        def volume(cls, jari, tinggi):
            return 22/7 * jari * jari * tinggi
        cls.volume = classmethod(volume)
class Luaspermukaandanvolume(metaclass=TabungMeta):
    pass
A = Luaspermukaandanvolume()
B = A.luaspermukaan(12, 2)
C = A.volume(3, 4)
print('Luas Permukaan Tabung\t:',B)
print('Volume Tabung\t\t:',C)