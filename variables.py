
# Working with variables
import os
os.system("cls")


# Declaring a variable and initialize it
# variables can still be re-declared.
f=0
g=0 # Local variable
print(f)

f = "abc"
print(f)

# Variables of different types cannot be combine
# print("This is a string " + 123)
print("This is a string "+ str(123))


# Global vs Local variables in functions
def someFunction():
    global g # Makes the variable global
    g = "def" # Local variable 
    print(g)

someFunction()
print(g)

del f # undefined a variable
print(f)