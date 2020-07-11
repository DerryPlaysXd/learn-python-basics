"""
Welcome to the third course of the Learn-Python-Basics project!

Here you will learn how to use if statements!
"""

# First we need to make a variable and since we already know how to make the user inputs we are going to make the user input something in:
aVar = input("Type 1 or 2:  "))

# Than we can make our first if statement:
if aVar == 1:
    print("You typed 1, good job!")
# If you need to add another if you use 'elif':
elif aVar == 2:
    print("You typed 2, good job!")
# If we want to do something in case the user writes something else than the ones we expected we use 'else':
else:  # If the user types for example '3' the program will print out 'You didn't type 1, neither you did type 2'
    print("You didn't type 1, neither you did type 2")

"""
This is the end of the course! Move on to another one!
"""
