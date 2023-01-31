'''
9.Python Program to Check Prime Number.
'''

def primeN(n):
    for i in range(2,n+1):
        if (i % n) == 0:
            f = True
            break
    if f:
        print("not prime")
    else:
        print("prime")

num = int(input("Enter Number: "))
primeN(num)