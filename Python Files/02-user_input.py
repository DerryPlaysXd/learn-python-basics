"""
Welcome to the second course of the Learn-Python-Basics project!

Here you will learn how to make the user put in their input!
"""

# First of all we need to make a variable and make the user input into the variable:
# Input without any modifier in front of it just saves the variable as string, that means it can't be used for math and anything like it
aVar = input("Input:    ")

# We can now print out the input:
print(aVar)

# If we want the user to use numbers, we need to convert the number into integer, let's say we want '1' for yes and '2' for no:
# If we add the 'int' modifier the input is now converted to integer, which means we can do some math and stuff like that with it
aVar = int(input("Yes(1), No(2):    "))

# Once again we can print the variable out:
print(aVar)

"""
This is the end of the course! Move on to another one!
"""