print("Stop Iteration")
try:
    def my_iterator():
        my_list = [1,2,3]
        iterator = iter(my_list)
        while True:
            item = next(iterator)
            print(item)
    my_iterator()
except StopIteration:
    print("Iterasi Selesai")

print("\nSyntax Error")
try:
   code = """
   print("Hello')
   """
   compiled.code = compile(code, "<string>", "exec")
except SyntaxError as e:
    print("Terjadi syntax error", e)

print("\nSystem Error")
try:
    a =10/0
except SystemError as e:
    print("Terjadi system error", e)
finally:
    print("Selesai!")