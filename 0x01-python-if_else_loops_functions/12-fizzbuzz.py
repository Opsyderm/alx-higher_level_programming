#!/usr/bin/python3
# 12-fizzbuzz.py


def fizzbuzz():
    """Prints the numbers from 1 to 100 separated by space.

    For multiples of three, prints Fizz in place of the number.
    For multiples of five, prints Buzz in place of the number.
    For multiples of three and five, print FizzBuzz in place of the number.
    """
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")

