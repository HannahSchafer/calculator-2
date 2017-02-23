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
   components = user_input.split(" ") ====> this will give us an list
   make components[1:] into integers
-determine which opperation is being asked for
    compare components[0] to possible opperators
        call appropriate function
"""

while True:
    continuing = raw_input("continue? ")
    if continuing[0].lower() == 'q':
        print "thanks, Byeee!"
        break
    else:
        user_input = raw_input("Enter prefix math: ")
        print user_input
