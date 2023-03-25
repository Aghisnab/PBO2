print("\nNama  : Aghisna Baihaqi")
print("NIM   : 210511034")
print("Kelas : TI21A(R1)\n\n")


class konversi():
    def __init__(self,K):
        self.kelvin = K

    def celcius(self):
        C = self.kelvin-273
        print(f'\n\nKelvin: {self.kelvin} K')
        print(f'Konversi Kelvin ke Celcius\n\t============\t\nCelcius: {(C)} C')

    def fahrenheit(self):
        F = ((self.kelvin-273)*(9/5))+32
        print(f'\nKelvin: {self.kelvin} K')
        print(f'Konversi Kelvin ke Fahrenheit\n\t============\t\nFahrenheit: {F} F')

    def reamur(self):
        R = (4/5)*(self.kelvin-273)
        print(f'\nKelvin: {self.kelvin} K')
        print(f'Konversi Kelvin ke Reamur\n\t============\t\nReamur: {R} Re\n')


kelvin1 = konversi(319)
kelvin1.celcius()
kelvin2 = konversi(292)
kelvin2.celcius()
kelvin2.fahrenheit()
kelvin2.reamur()

