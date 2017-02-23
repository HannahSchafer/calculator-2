"""TODO
-alter calc function
    make list of nums (done)
    feed list into function
-change params on functions
-change the body the arithmetic functions
    iteration!
"""


def add(list):
    counter = 0
    for item in list:
        counter += item
    return counter


def subtract(list):
    counter = list[0]
    for item in list[1:]:
        counter -= item
    return counter


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    # Need to turn at least argument to float for division to
    # not be integer division
    return float(num1) / float(num2)


def square(num1, junk):
    # Needs only one argument
    return num1 * num1


def cube(num1, junk):
    # Needs only one argument
    return num1 * num1 * num1


def power(num1, num2):
    return num1 ** num2  # ** = exponent operator


def mod(num1, num2):
    return num1 % num2
