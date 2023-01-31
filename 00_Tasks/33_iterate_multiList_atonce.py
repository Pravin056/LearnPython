'''
33.Given a two Python list. Iterate both lists simultaneously such that
list1 should display item in original order and list2 in reverse order.
    list1=[10,20,30,40]
    list2=[100,200,300,400]
'''

list1=[10,20,30,40]
list2=[100,200,300,400]
list3=list2.reverse()

'''
Enumerate() method adds a counter to an iterable and returns it in a form of enumerating object.
This enumerated object can then be used directly for loops or converted into a list of tuples using the list() method.
'''
for i, x in enumerate(list1):
    print(x, list2[i])
