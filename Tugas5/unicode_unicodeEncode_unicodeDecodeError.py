print("Unicode Error")
try:
    string = "Hello NJ, 엑소"#엑소 bahasa korea EXO
    string.encode('ascii')
except UnicodeError:
    print("Terjadi kesalahan Unicode! String mengandung karakter non-ASCII")
except Exception as e:
    print("Terjadi kesalahan:",e)

print("\nUnicode Decode Error")
try:
    file = open("file.txt", "r", encoding="utf-8")
    content = file.read()
    file.close()
    print(content)
except UnicodeDecodeError:
    print("Terjadi kesalahan dalam menguraikan karakter Unicode:")
except Exception as e:
    print(e)

print("\nUnicode Encode Error")
try:
   text = "Halo, Aghisna! \u2713"
   encode_text = text.encode("ascii")
   print(encoded.text)
except TabError:
    print("Terjadi kesalahan dalam mengkodekan karakter Unicode")
except Exception as e:
    print(e)

print("\nUnicode Translate Error")
try:
   text = "Halo, 엑소!"
   translated_text = text.translate(str.maketrans("",""), "EXO")
   print(translated_text)
except TabError:
    print("Terjadi kesalahan dalam menerjemahkan karakter Unicode")
except Exception as e:
    print(e)