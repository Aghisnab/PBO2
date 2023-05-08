print("Tab Error")
try:
   code = """
if True:
    print('Hello')
        print('Aghisna')
   """
   compiled_code = compile(code, "<string>", "exec")
   exec(compiled_code)
except TabError:
    print("Terjadi Tab Error")
except Exception as e:
    print(e)

print("\nSystem Exit")
try:
    import sys
    print("Sebelum sys.exit()")
    sys.exit("Pesan Keluar")
    print("Setelah sys.exit()")
except SystemExit as e:
    print("Terjadi system exit:",e)

print("\nUnbound Local Error")
try:
    def fungsi():
        x = x + 1
    fungsi()
except UnboundLocalError as e:
    print("Terjadi kesalahan:", str(e))
