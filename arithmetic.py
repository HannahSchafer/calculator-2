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


def multiply(list):
    counter = 1
    for item in list:
        counter *= item
    return counter


def divide(list):
    # Need to turn at least argument to float for division to
    # not be integer division
    counter = float(list[0])
    for item in list[1:]:
        counter /= float(item)
    return counter


def square(list):
    # Needs only one argument
    counter = []
    for item in list:
        counter.append(item**2)
    return counter


def cube(num1, junk):
    # Needs only one argument
    return num1 * num1 * num1


def power(num1, num2):
    return num1 ** num2  # ** = exponent operator


def mod(num1, num2):
    return num1 % num2
