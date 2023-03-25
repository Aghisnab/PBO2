print("\nNama  : Aghisna Baihaqi")
print("NIM   : 210511034")
print("Kelas : TI21A(R1)\n\n")


class konversi():
    def __init__(self,F):
        self.fahrenheit = F

    def celcius(self):
        C = (5/9)*(self.fahrenheit-32)
        print(f'\n\nKelvin: {self.fahrenheit} F')
        print(f'Konversi Fahrenheit ke Celcius\n\t============\t\nCelcius: {(C)} C')

    def kelvin(self):
        K = (5/9)*(self.fahrenheit-32)+273
        print(f'\nKelvin: {self.fahrenheit} F')
        print(f'Konversi Fahrenheit ke Kelvin\n\t============\t\nKelvin: {K} K')

    def reamur(self):
        R = (4/9)*(self.fahrenheit-32)
        print(f'\nKelvin: {self.fahrenheit} F')
        print(f'Konversi Fahrenheit ke Reamur\n\t============\t\nReamur: {R} Re\n')


fahrenheit1 = konversi(315)
fahrenheit1.celcius()
fahrenheit2 = konversi(275)
fahrenheit2.celcius()
fahrenheit2.kelvin()
fahrenheit2.reamur()

