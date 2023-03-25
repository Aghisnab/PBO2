print("\nNama  : Aghisna Baihaqi")
print("NIM   : 210511034")
print("Kelas : TI21A(R1)\n\n")


class konversi():
    def __init__(self,R):
        self.reamur = R

    def celcius(self):
        C = self.reamur*(5/4)
        print(f'\n\nReamur: {self.reamur} Re')
        print(f'Konversi Reamur ke Celcius\n\t============\t\nCelcius: {(C)} C')

    def fahrenheit(self):
        F = (9/4)*self.reamur+32
        print(f'\n\nReamur: {self.reamur} Re')
        print(f'Konversi Reamur ke Fahrenheit\n\t============\t\nFahrenheit: {F} F')

    def kelvin(self):
        K = (5/4)*self.reamur+273
        print(f'\n\nReamur: {self.reamur} Re')
        print(f'Konversi Reamur ke Kelvin\n\t============\t\nKelvin: {K} Re\n')


reamur1 = konversi(12)
reamur1.celcius()
reamur2 = konversi(29)
reamur2.celcius()
reamur2.fahrenheit()
reamur2.kelvin()

