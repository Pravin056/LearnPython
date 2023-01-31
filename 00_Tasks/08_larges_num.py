'''
8.Python Program to Find the Largest Among Three Numbers.
'''

a = int(input("Enter First Number: "))
b = int(input("Enter First Number: "))
c = int(input("Enter First Number: "))

list1 = [a,b,c]
d = max(list1)
print("largest number among {},{},{} is {}".format(a,b,c,d))