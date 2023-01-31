'''
31.Remove multiple elements from a list in Python.(11,5,17,18,23,50)
'''

list1 = [12,49,3,2,44,56,44,67,66,33]
list1 = [ elem for elem in list1 if elem % 2 != 0]
print(list1)


del list1[1:2]
print(list1)

for i in list1:
    if i % 2 != 0:
        list1.remove(i)
print(list1)