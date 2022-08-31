class Customer:

    #Constructor
    def __init__(self, name, account_type):
        self.name = name
        self.account_type = account_type

    # A to string method 
    def __str__(self):
        print('Converting to String')
        return ""

    # Compares two objects
    def __eq__(self, other):
        if self.name == other.name and self.account_type == other.account_type:
            return True
        return False
        
#instatiating a the class Customer
c =  Customer('Mumbod','Diamond')

print(c.name, c.account_type)
