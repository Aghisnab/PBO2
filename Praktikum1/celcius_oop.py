print("\nNama  : Aghisna Baihaqi")
print("NIM   : 210511034")
print("Kelas : TI21A(R1)\n\n")


class konversi():
    def __init__(self,celcius):
        self.celcius = celcius

    def fahrenheit(self):
        F = (5/9)*self.celcius+32
        print(f'\n\nCelcius: {self.celcius} C')
        print(f'Konversi Celcius ke Fahrenheit\n\t============\t\nFahrenheit: {F} F')

    def kelvin(self):
        K = self.celcius+273
        print(f'\n\nCelcius: {self.celcius} C')
        print(f'Konversi Celcius ke Kelvin\n\t============\t\nKelvin: {K} K')

    def reamur(self):
        R = (4/5)*self.celcius
        print(f'\n\nCelcius: {self.celcius} C')
        print(f'Konversi Celcius ke Reamur\n\t============\t\nReamur: {R} Re')

celcius1 = konversi(75)
celcius1.fahrenheit()
celcius2 = konversi(60)
celcius2.kelvin()
celcius3 = konversi(90)
celcius3.reamur()
