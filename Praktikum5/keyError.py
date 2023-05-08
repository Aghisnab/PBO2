dictionary = {"Mei": 5, "April": 4, "Februari": 2}
try:
    value = dictionary["Maret"]
except KeyError:
    print("Key yang diminta tidak ditemukan pada dictionary!")