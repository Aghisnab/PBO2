list_bulan = ["Januari", "Februari", "April", "Mei"]

try:
    value = list_bulan[5]
except IndexError:
    print("Index yang diminta melebihi jumlah elemen dalam list!")