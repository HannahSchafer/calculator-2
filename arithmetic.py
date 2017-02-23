"""TODO
-alter calc function
    make numbers of nums (done)
    feed numbers into function
-change params on functions
-change the body the arithmetic functions
    iteration!
"""


def add(numbers):
    counter = 0
    for item in numbers:
        counter += item
    return counter


def subtract(numbers):
    counter = numbers[0]
    for item in numbers[1:]:
        counter -= item
    return counter


def multiply(numbers):
    counter = 1
    for item in numbers:
        counter *= item
    return counter


def divide(numbers):
    # Need to turn at least argument to float for division to
    # not be integer division
    counter = float(numbers[0])
    for item in numbers[1:]:
        counter /= float(item)
    return counter


def square(numbers):
    # Needs only one argument
    counter = []
    for item in numbers:
        counter.append(item**2)
    return counter


def cube(numbers):
    # Needs only one argument
    counter = []
    for item in numbers:
        counter.append(item**3)
    return counter


def power(numbers):
    new_expo = 1
    while len(numbers) > 0:
        exponent = numbers.pop()
        new_expo =numbers[-1]**exponent
    return new_expo





def mod(num1, num2):
    return num1 % num2

"""
def power(numbers):
    def recursor(num, numbers_2):
        #base case
        if len(numbers_2) == 1:
            return num**numbers_2[0]
        elif len(numbers_2) < 1:
            print "You need at least 2 numbers."
        else: 
            new_num = numbers_2.pop(0)
            return num ** recursor(new_num, numbers_2)
    return recursor(numbers[0], numbers[1:])
"""
