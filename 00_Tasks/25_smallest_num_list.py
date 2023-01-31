'''
25.Python program to find smallest number in a list.
'''

def smallestele(list1):
    list1.sort()
    return list1[0]

list2 = [43,56,32,65,23,7]
print(smallestele(list2))

#------------------------------
def smallestele2(list1):
    return min(list1)

list2 = [43,56,32,65,23,7]
print(smallestele2(list2))