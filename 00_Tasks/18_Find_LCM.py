'''
18.Python Program to Find LCM.

The least common multiple (L.C.M.) of two numbers is the smallest positive integer
that is perfectly divisible by the two given numbers.
For example, the L.C.M. of 12 and 14 is 84.
'''

def lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = lcm(n1, n2)

print("The L.C.M. of {} and {} is {}".format(n1,n2,n3))
