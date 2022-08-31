class Computation:
    def __init__(self):
        print('')

    def Factorial(self, n):
        product = 1
        for i in range(1,n):
            product = product*i;

        print(n,' Factorial = ', product)

    def Sum(self,n):
        total = 0
        for i in range(1,n):
            total +=i
        print('The total is ',total)

    def testPrim(self, n):
        print('')
        

computation =  Computation()
computation.Factorial(5)
computation.Sum(5)
