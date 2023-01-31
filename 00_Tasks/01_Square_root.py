'''
01. Python program to find square root
'''

a = int(input("Enter Number : "))
# # b = a * a
# # print("root of",a,"is",b)
# j = 1
# r = 1
# for i in range(a+1):
#     if (a == 0 or a == 1):
#         p = a
#     elif r <= a:
#         j += 1
#         r = j * j
#         p = j - 1
# print("Square root of",a,"is",p)

s = a**0.5
print("the square root of %0.0f is %0.2f" %(a,s))