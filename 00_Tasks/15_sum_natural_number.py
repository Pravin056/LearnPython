'''
15.Python Program to Find the Sum of Natural Numbers.
'''

num = int(input("Enter NUmber: "))
num2 = num

if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   while(num > 0):
       sum += num
       num -= 1
   print("The sum of {} is {}".format(num2,sum))