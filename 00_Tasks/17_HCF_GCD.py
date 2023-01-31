'''
17.Python Program to Find HCF or GCD.
H.C.F. = Highest Common Factor
G.C.D. = Greatest Common Divisor
'''

def hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf1 = i
    return hcf1

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = hcf(n1, n2)

print("The H.C.F. of {} and {} is {}".format(n1,n2,n3))

#GCD
def gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

n4 = gcd(n1,n2)
print("The G.C.D. of {} and {} is {}".format(n1,n2,n4))

