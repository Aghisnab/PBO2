try:
    with open("unexist_file.txt") as file:
        data = file.read()
except FileNotFoundError:
    print("File Not Found!")