# A class is the blueprint of an object


class FirstClass:

    def __init__(self):
        b = 90
    """This is the docstring"""  # It can se accessed using __doc__ variable
    a = 10

    def printtext(self):
        print("I am function")

    def printfunc(self):
        print("I am Function")


fir = FirstClass()
print(fir.b)
print(fir.__doc__)
print(fir.printfunc())