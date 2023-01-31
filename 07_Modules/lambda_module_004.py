from functools import *

def in_square(x):
    return x*x
print(in_square(5))

#syntax : lambda arg:expression
v=lambda x,y,m,n:x*n
print(v(5,6,8,4))

##filter()

#iterable vc iterator vs iter
num = [3,4,6,8,4,6,3,88,55,3]

#with function
def is_even(n):
    return n%2==0
even = list(filter(is_even,num))
print(even)

#with lambda
even = list(filter(lambda n:n%2==0,num))
print(even)

##map()
#with function
def update(n):
    return n*2
square2 = list(map(update,even))
print(square2)

#with lambda
square2 = list(map(lambda n:n*2,even))
print(square2)

##reduce
#with function
def add_all(a,b):
    return a+b

added = reduce(add_all,square2)
print(added)

#with lambda
added = reduce(lambda a,b:a+b,square2)
print(added)

l2 = [22,33,55,88,99,123,258,456,87,79] #odd,map,reduce

odd1 = list(filter(lambda n:n%2==1,l2))
print(odd1)

map1 = list(map(lambda n:n*2,odd1))
print(map1)

reduce1 = reduce(lambda a,b:a*b,map1)
print(reduce1)




