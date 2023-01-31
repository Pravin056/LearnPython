'''
13.Python Program to Check Armstrong Number.
An armstrong number in python is a positive integer of base n, and the sum of each digit of the Armstrong number of
order n is equal to the number itself.

For example, let us consider ABC of order ‘n’ then ABC is an Armstrong number if:
ABC= An+Bn+Cn

Let us consider an Armstrong number 371, the sum of the cubes of each digit of 371 is equal to the number itself
371= 3**3 + 7**3+ 1**3
'''

num = int(input("Enter Number: "))
lenn = len(str(num))
sum = 0
temp = num
while temp > 0:
    dg = temp % 10
    sum += dg**lenn
    temp //= 10
if sum==num:
    print(num,"is armstrong number")
else:
    print(num, "is not armstrong number")
