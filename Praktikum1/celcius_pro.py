print("\nNama  : Aghisna Baihaqi")
print("NIM   : 210511034")
print("Kelas : TI21A(R1)\n\n")

def fahrenheit(C):
    F = (5/9)*C+32
    return F

def kelvin(C1):
    K = C1+273
    return K

def reamur(C2):
    Re = (4/5)*C2
    return Re

C = 75
Fah = fahrenheit(C)
print(f'\n\nCelcius: {C} C')
print(f'Konversi Celcius ke Fahrenheit\n\t============\t\nFahrenheit: {Fah} F')

C1 = 60
Kel = kelvin(C1)
print(f'\n\nCelcius: {C1} C')
print(f'Konversi Celcius ke Kelvin\n\t============\t\nKelvin: {Kel} K')

C2 = 90
Rea = reamur(C2)
print(f'\n\nCelcius: {C2} C')
print(f'Konversi Celcius ke Reamur\n\t============\t\nReamur: {Rea} Re')