#DICT
'''
Data Type Name      |Sign     | I or M        |Indexed      |Diff Data Types        |Duplicate
--------------------------------------------------------------------------------------------------
Dict                {}        key - Immutable   Un-order          Allow                  Allow
                              value - mutable

We can create keys with 01. Number | 02. Alphabet  | 03. Roman Numbers
we can use tuple as key in dictionary
Methods : --------------------------------------------------------------------------------------------------------------------------
clear()  |  copy()  |  fromkeys()  |  get()  |  items()  |  keys()  |  pop()  |  popitem()  |  setdefault()  |  update()  |  values()
'''
#in pair of key and value
#dict is unordered
#ex:like map

# a={}
# #check Type
# print(a,type(a))
# a = {1:"Python",2:"course",3:"i like",1:"java"}
# print(a)


# d1 = {1:"Python",2:"course",3:"i like",1:"java"} #allow number key also
# print(d1,type(d1))
# print(d1.values())
# print(d1.keys())
#
# #using dict() create one dict
# Dict={}
# print(Dict)
# D1=dict({1:"python",2:"course",3:"i like"})
# Dict=({1:"python",2:"course",3:"i like"})
# print(Dict)
#
# print(Dict[3],Dict[1],Dict[2])
# print(Dict.keys())

#creating nested dictionary

d2={1:"Python",2:"course",3:{'a':'welcome','b':'to','c':'quastech'}}
print(d2)


#adding element
d3={}
print(d3)

d3[0]="Welcome"
d3[1]="to"
d3[2]="quastech"
d3['a']=12
d3['b']=[1,2,3,45,6]
print(d3)

#accessing
print(d3['a'])

#accessing using get()
print(d3.get('b'))
a = d3.get("b")
print(a[3])
#we can use tuple as key in dictionary

#initial dict
d5={5:"welcome",6:"quastech",7:"institute","A":{1:"Python",2:"Course"},"B":{1:"java",2:"course"}}
print(d5)

#Deleting using del key
del d5[7] #how to delete key
del d5["A"][1] #How to delete nested key
print(d5)
#
# #pop
d7={5:"welcome",6:"quastech",7:"institute","A":{1:"Python",2:"Course"},"B":{1:"java",2:"course"}}
e=d7.pop(6)
print(e)
print(d7)

#popitems
v=d7.popitem()
print(v)
print("artibitrary values",d7)

# d7.clear()
# print(d7)

print(d5.items)

#task: get max vakue of each key
s={'a':[11,22,33], 'b':[44,77,99], 'c':[99,200,100,]}




