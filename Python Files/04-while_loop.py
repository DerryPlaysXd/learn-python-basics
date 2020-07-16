"""
Welcome to the fourth course of the Learn-Python-Basics project!

Here you will learn how to create and use the while loop!
"""

# First we need to declare a variable for a while loop, which defines the number of circles.
countVar = 0

# This code is a start of while loop. The template is "while STATEMENT:". While the "STATEMENT" is equal to "True", code below is repeating.
while countVar < 5:

# This code print a short message for user about successfull repeating of code in WHILE block.
# In this case, varible "count" doesn't need to convert to string, because it's separated by comma from string "Text".
	print("Text", countVar+1)

# This is the same as "count = count + 1". It's shorter and faster option for increasing a varible by 1.
# Without this line of code, while loop goes to infinity.
	countVar += 1

# And finally print for check, what we executed.
print("END!")

"""
This is the end of the course! Move on to another one!
"""
