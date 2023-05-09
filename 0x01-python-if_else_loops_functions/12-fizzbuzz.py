#!/usr/bin/python3
def fizzbuzz():
    for fig in range(1, 101):
        if fig % 3 == 0 and fig % 5 == 0:
            print("FizzBuzz ", end="")
        elif fig % 5 == 0:
            print("Buzz ", end="")
        elif fig % 3 == 0:
            print("Fizz ", end="")
        else:
            print("{} ".format(fig), end="")
