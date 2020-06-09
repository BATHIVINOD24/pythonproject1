"""A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)"""

x = 5 # x is of type int
y = "John" # y is now of type str
z = 'Sally' # String variables can be declared either by using single or double quotes: (y and z are same)
print(x)
print(y)
print(z)

#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"

#Python allows you to assign values to multiple variables in one line:
x,y,z = "orange", "banana", "cherry"
print(x)
print(y)
print(z)

#And you can assign the same value to multiple variables in one line:
x = y = z = "orange"
print(x)
print(y)
print(z)

#To combine both text and a variable, Python uses the + character:
x = "awesome"
y = "super"
print("python is " + x)
print("python is " + y)

#You can also use the + character to add a variable to another variable:
x = "python is "
y = "awesome"
z = x + y
print(z)

#For numbers, the + character works as a mathematical operator:
x = 5
y = 7
print(x+y)

#If you try to combine a string and a number, Python will give you an error:
x = 5
y = "John"
print(x+y)

"""Variables that are created outside of a function (as in all of the examples above) are known as global variables.
Global variables can be used by everyone, both inside of functions and outside."""
