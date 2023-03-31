class jajan:
    def __init__(self, fare):
        self.fare = fare

    def __add__(self, other):
        return self.fare+other.fare

seblak = jajan(10)
basoaci = jajan(15)
total = seblak+basoaci
print(f'\nHarga Total: {str(total)}k\n')