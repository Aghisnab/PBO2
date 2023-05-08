print("Assestion Error")
try:
    def calculate_BMI(berat, tinggi):
        assert tinggi > 0
        bmi = berat / (tinggi/100)**2
        return bmi

    bmi1 = calculate_BMI(52, -155)
except AssertionError:
    print("Tinggi tidak boleh bernilai negatif!\n")

print("Import Error")
try:
    import bar
except ImportError:
    print("ModulNotFoundError:No module named 'bar'\n")

print("EOF Error")
try:
    n = input("Ketikkan sesuatu:") 
    print(f'input {n}')    
except EOFError:
    print('Tidak Ada Input!')
