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
#Create a variable outside of a function, and use it inside the function
x = "awesome"
def myfunc():
    print("python is " + x)
myfunc()

"""If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. 
The global variable with the same name will remain as it was, global and with the original value."""
#Create a variable inside a function, with the same name as the global variable
x = "awesome"
def myfunc():
    print("python is " + x)
myfunc()

"""If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. 
The global variable with the same name will remain as it was, global and with the original value."""
#Create a variable inside a function, with the same name as the global variable
x = "awesome"
def myfunc():
    x = "fantastic"
    print("python is " + x)
myfunc()

print("python is " + x)

"""Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
To create a global variable inside a function, you can use the global keyword."""
#If you use the global keyword, the variable belongs to the global scope:
def myfunc():
    global x
    x = "fantastic"
myfunc()

print("python is " + x)

#Also, use the global keyword if you want to change a global variable inside a function.
#To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "awesome"
def myfunc():
    global x
    x = "fantastic"
myfunc()

print("python is " + x)