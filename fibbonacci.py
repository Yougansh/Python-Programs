'''
Program for fibbonacci series
'''

def printFibbonacciSeries(a):
    sum = 0
    b = 1
    c = 0
    for i in range(1,a+1,1):
        sum = c + b
        print(sum)
        b=c
        c=sum        

print("Fibbonaaci Series for 10 numbers:")
printFibbonacciSeries(10)
