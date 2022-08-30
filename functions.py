
# Working with functions

import os
os.system("cls")


# Defining a function
# Funtions are defined with the def keyword
# Python uses a column and the next line is indented
def func1():
    print("I am a function")


# Function that takes arguments
def func2(arg1, arg2):
    print(arg1," ", arg2)


# Function that returns a value
def cube(x):
    return x*x*x


# A function that takes arguments and one of the arguments have default value
def power(num, x = 1 ):
    result = 1
    for i in range(x):
        result = result * num
    return result

# A function with variable number of arguments
# The * character means any number of arguments can be passed
# The variable argument can be combine with a different argument 
# but it must be the last argument.
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result


func1()
print(func1())
print(func1)

func2(10,20)
print(func2(10,20))

print(cube(3))

print(power(2))
print(power(2,3))

# Python lets you call functions with their named parameters along with their values
print(power(x=3, num=2)) 

print(multi_add(10,4,5,10,4))