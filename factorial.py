
'''
Program for factorial
'''

def findFactorial(a):
    fact = 1
    for i in range(1,a+1,1):
        fact = fact * i
    print(fact)

findFactorial(4)
