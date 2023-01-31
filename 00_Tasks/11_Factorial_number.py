'''
11.Python Program to Find the Factorial of a Number.

The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1
For example: calculate the factorial of 5
5! = 5 × 4 × 3 × 2 × 1 = 120
'''

num=int(input("Enter Number: "))
# fact=1
# for i in range(1,num+1):
#     fact = fact*i
# print("Factorial of",num,"is",fact)

#Factorial in Function

def fact2(n):
    fact=1
    for i in range(1,n+1):
        fact = fact*i
    print("Factorial of",n,"is",fact)
fact2(num)

#--------------------------------------------
# def fact(x):
#     if x == 1:
#         return 1
#     else:
#         return(x*fact(x-1))
#
# num=int(input("Enter Number: "))
# res=fact(num)
# print(res)