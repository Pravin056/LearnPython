'''
10.Python Program to Print all Prime Numbers in an Interval.

Note: A Prime Number is a number that cannot be made by multiplying other whole numbers.
A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers

Examples:
    6 is not a prime number because it can be made by 2×3 = 6
    37 is a prime number because no other whole numbers multiply together to make it.
'''

# range
start = int(input("Start: "))
end = int(input("End: "))
#
# for i in range(start,end+1):
#     if i > 1:  #all prime numbers are greater than 1
#         for j in range(2,i):
#             if (i % j) == 0: #check for factors - Prime number
#                 break
#         else:
#             print(i,end=" ")

#in Function
def primeN(s,e):
    for i in range(s,e+1):
        if i > 1:
            for j in range(2,i):
                if (i % j) == 0:
                    break
            else:
                print(i,end=" ")

primeN(start,end)
