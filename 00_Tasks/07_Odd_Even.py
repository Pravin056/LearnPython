'''
7.Python Program to Check if a Number is Odd or Even.
'''

num = int(input("Enter Number: "))

if num==0:
    print("Number is Zero")
elif num%2==0:
    print("Number is Even")
else:
    print("Number is Odd")

# in Function
def oddeve(n):
    if n == 0:
        print("Number is Zero")
    elif n % 2 == 0:
        print(n,"Number is Even")
    else:
        print(n,"Number is Odd")

oddeve(num)