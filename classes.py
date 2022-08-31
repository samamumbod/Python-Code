# Working with classes
# OOP IN PYTHON

import os
os.system("cls")

class myClass():

    # the first argument is the self argument
    # the self argument referes to the object itself
    def method1(self):
        print("myClass method1")
    
    def method2(self, someString):
        print("myClass method2 "+someString)


# Inheritanc
class anotherClass(myClass):

    def method1(self):
        myClass.method1(self)
        print("anotherClass method1")
    
    # Polymorphism
    def method2(self, someString):
        print("anotherClass method2 ")


def main():
    print()
    c = myClass()
    c.method1()
    c.method2("This is a string")


    c2 = anotherClass()
    c2.method1()
    c2.method2("This is a String")


if __name__ == "__main__":
    main()