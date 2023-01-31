a={}
b=set() #How to create empty set in python
print(type(a))
print(type(b))

product1 = [44,66,77,88,44,77]
print(type(product1))

set5 = set(product1) #type casting
print(set5,type(set5))

set2 = {3,5,4,7,8,9,7}
set2.remove(8)
print(set2)

set2.pop()
print(set2)

set2.discard(5)
print(set2)

#---------------------------
a=set()
b={1,2,4,6,8}
set3={1,66,88,99}
a.update(set3)
b.update(set3)
print(a)
print(b)

set3.add(33)
print(set3)

s1 = {1,2,3,4,5}
s2={1,2,3,4,5,6,7,8,9,10}

print(s2.issubset(s1))
print(s1.issubset(s2))
print(s1.intersection(s2))
print(s1.union(s2))

set2.clear()
print(set2)

s55=set()
print(s55,type(s55))
for i in range(1,6):
    s55.add(i)
print(s55)

k= {x for x in range(0,6)} #create empty set with iterable objects
print("k:",k)

s22=frozenset()
print(s22,type(s22))

num=[1,2,3,45,555,6,6,7,7,766] #Mutable
fnum = frozenset(num)
print(fnum,type(fnum))

# fnum[4]=666 #TypeError: 'frozenset' object does not support item assignment
# print(fnum)

s33 = {'a':10,'Name':'Quastech',1:'abc'}
print(s33,type(s33))
fnum1=frozenset(s33)
print(fnum1,type(fnum1))


a={'a':1,'b':2,1:'a',2:'b'}
#exptected output a={1:'a',2:'b'}
#remove string key from dictionary
