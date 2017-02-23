"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
"""TODO
-enable quitting
-ask for input and save it to a variable
    user_input = raw_input
-tokenize string
   components = user_input.split(" ") ====> this will give us a list
   make components[1:] into integers
-determine which opperation is being asked for
    compare components[0] to possible opperators
        call appropriate function
"""

while True:
    #ask user for input
    user_input = raw_input("Enter prefix math: ")
    #split input into individual string components
    components = user_input.split(" ")
    #turn stringed numbers into integers and append them into their own list
    nums_list = []
    for item in components[1:]:
        item = int(item)
        nums_list.append(item)
    #enabling add function
    if components[0] == "+":
        print add(nums_list[0], nums_list[1])
    #enable subtract
    if components[0] == "-":
        print subtract(nums_list[0], nums_list[1])
    # continue or quit?
    continuing = raw_input("continue? ")
    if continuing[0].lower() == 'q':
        print "thanks, Byeee!"
        break
