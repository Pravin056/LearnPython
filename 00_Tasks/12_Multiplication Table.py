'''
12.Python Program to Display the multiplication Table Code.
'''

n = int(input("Enter Number: "))
print("Table of {}".format(n))

#List Comprehension Method
table=[x*n for x in range(1,11)]
print(table)

#for loop method
for i in range(1,11):
    t = n*i
    print(t,end=" ")