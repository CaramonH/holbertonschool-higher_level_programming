#!/usr/bin/python3
def fizzbuzz():

    for i in range(1, 101):
        fizztest = i % 3
        buzztest = i % 5
        if fizztest == 0 and buzztest == 0:
            print("FizzBuzz ", end='')
        elif fizztest == 0:
            print("Fizz ", end='')
        elif buzztest == 0:
            print("Buzz ", end='')
        else:
            print("{} ".format(i), end='')
