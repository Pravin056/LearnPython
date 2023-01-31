'''
24.Python program to interchange first and last elements in a list.
'''

def interchange(List1):
    List1[0], List1[-1] = List1[-1], List1[0]
    return List1

List2 = [34, 12, 78, 67, 99]
print(interchange(List2))