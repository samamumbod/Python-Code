
#
# Example file for HelloWorld
#
import os 
os.system('cls') # Clears the screen.


# Defining a function
# Python uses white space to figure which lines of codes 
# belong to scope block
''' - Python does not have this notion of curly braces. 
    - python uses indentation to indicate where the 
    line of code belongs.
'''
def main():
    print("Hello World")
    name = input("What is your name: ") # Reads a name
    print("Nice to meet you, ", name) # Prints user name


'''
Unlike in Java and C, Python does not look for a function called main
when the program starts.

'''

# it checks if the property name is equal to main
# It can also be used to load the a module
if __name__ =="__main__": 
    main()