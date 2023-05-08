print("Not Implemented Error")
try:
    class Animal:
        def make_sound(self):
            raise NotImplementedError("Class doesn't have abstract method")
    class Cat(Animal):
        pass
    myCat = Cat()
    print(myCat.make_sound())
except NotImplementedError as e:
    print(e)

print("\nOver Flow Error")
try:
    import math
    result = math.exp(9000)
    print(result)
except OverflowError as e:
    print(e)

print("\nRecursion Error")
try:
    def factorial(n):
        if n == 0:
            return 0
        else:
            return n*factorial(n-1)
    hasil = factorial(1000)
    print(hasil)   
except RecursionError as e:
    print(e)
