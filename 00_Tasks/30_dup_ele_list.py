'''
30.Program to print duplicates from a list of integers.
'''

def dup(list1):

    list2 = []
    list3 = []

    for i in list1:
        if i not in list2:
            list2.append(i)
        elif i not in list3:
            list3.append(i)
    return list3

list1 = [1,4,4,5,6,6,7,3,2,2,8,9,0,6,5,9]
print(dup(list1))