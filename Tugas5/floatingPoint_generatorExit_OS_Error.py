print("Floting Point Error")
try:
    a = 1.0
    b = 0.0
    result = a/b
except ZeroDivisionError:
    print("Pecahan tidak bisa dibagi dengan 0\n")

print("Generator Exit")
def my_generator():
    try:
        yield 1
        yield 2
        yield 3
    except GeneratorExit:
        print("Generator Closed\n")
gen = my_generator()
print(next(gen))
print(next(gen))
gen.close()

print("OS Error")
import os
try:
    os.rmdir("/path/to/nonempty_directory")
except OSError as e:
    print(f"Error: {e}")
finally:
    print("Selesai!")