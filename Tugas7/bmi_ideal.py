class MetaCalculateBMI(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        
        def Male(cls, tinggi):
            return (tinggi - 100) - (tinggi - 100) * 10/100
        cls.Male = classmethod(Male)

        def Female(cls, tinggi):
            return (tinggi - 100) - (tinggi - 100) * 15/100
        cls.Female = classmethod(Female)

class Ideal(metaclass=MetaCalculateBMI):
    pass

A = Ideal()
wanita = A.Female(155)
pria = A.Male(195)

print('\nBerdasarkan Perhitungan Broca berat IDEAL anda ...')
print("Wanita : ",wanita)
print("Pria   : ",pria)