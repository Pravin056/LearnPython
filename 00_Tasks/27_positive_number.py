'''
27.Python program to print all positive numbers in a range.
'''

def pos(n1,n2):
    l = []
    for i in range(n1,n2+1):
        if i >= 0:
            l.append(i)
    return l

n1 = int(input("Enter start number"))
n2 = int(input("Enter end number"))
print(pos(n1,n2))