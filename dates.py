
# Working with dates

import os
os.system("cls")

from datetime import date
from datetime import time
from datetime import datetime



def main():

    # Date Object
    # Prints the current date
    today = date.today()
    print("Today's date : ", today)

    # Print out individual components
    print("Date components: ", today.day, today.month, today.year)

    # Print the weekday (Mon=0 and Sun=6)
    print("Today's weekday number : ", today.weekday())
    days = ["Mon","Tue", "Wed","Thu","Fri","Sat","Sun"]
    print("Week day is : ", days[today.weekday()])


    # DateTime Object
    today = datetime.now()
    print("The current date time: ",today)

    #Get the time
    t = datetime.time(datetime.now())
    print(t)

if __name__=="__main__":
    main()

