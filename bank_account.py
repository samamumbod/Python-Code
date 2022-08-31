class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(amount, ' has just been added to your account')
        print('New account balance = ', self.balance)

    def withDraw(self,amount):
        self.balance -= self.bankFee(amount)
        print(amount, ' has just been deducted from your account')
        print('Charges of 5% applied.')
        print('New account balance = ', self.balance)

    def bankFee(self, amount):
        fee = 0.05 * amount
        totalAmount = fee + amount
        return totalAmount

    def display(self):
        print('Account Number: ', self.accountNumber)
        print('Name: ', self.name)
        print('Balance: ', self.balance)


bAccount = BankAccount(5460, 'Mumbod', 100000)
bAccount.display()
print('')
bAccount.deposit(50000)
print('')
bAccount.withDraw(25000)
print('')


