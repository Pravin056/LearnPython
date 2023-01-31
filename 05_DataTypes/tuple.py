a=1,2,3,5
print(a,type(a))

b=(1)
print(b,type(b))

c=(1,)
print(c,type(c))

c=1,
print(c,type(c))

'''
Tuple separated by comma
'''

t=(12,"Python",5.9,333,"a") #diff datatypes allowed
print(t[0]) #allowed Indexing

t1 = ("python","interpreater")
t2 = (22,44,2.9,56)
t3 = t1 + t2
print(t3)

#t4 = ("python","course",22,44,2.9,56,22,22)

'''
t4[1]="course"
print(t4)
TypeError: 'tuple' object does not support item assignment

# t4[2]=23
# print(t4)

t4.pop()
print(t4)
'''
t4 = ("python","course",22,44,2.9,56,22,22)
print(len(t4))
print(t4.count(22))

for i in t4:
    print(i)

#simillar to append
t5 = (1,2,3,4,5)
t6 = (44,66,77,88,99)

r1 = (t5,t6) #append
print(r1)
r2 = (t5+t6) #extend
print(r2)

print(r1[1])
print(r2[1])

#sort element in tuple using sorted() method
a = 933,55,66,77,88
b = 'a','m','h','i'

#using sorted() method
print(sorted(a))
print(sorted(b))

t9 = (3455,66,77,888,999,333)
print("max",max(t9))
print("min",min(t9))
print("len",len(t9))
print("reverse",t9[::-1])

#swith the tuple value
m = (11,12,13,14,15) #swith the 13 to 45



