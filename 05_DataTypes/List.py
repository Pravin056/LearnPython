'''
Data Type Name      |Sign     | I or M        |Indexed      |Diff Data Types        |Duplicate
--------------------------------------------------------------------------------------------------
List                []          Mutable         Indexed       Allow                   Allow
'''
# #Indexing   0        1        2       3        4       5       6
# list1 = ["apple","banana","cherry","mango","papaya","kiwi","grapes"]
# #rev Index  -7      -6       -5      -4        -3      -2      -1
# #Index
# print(list1[0]) #Index
# print(list1[-1]) #Reverse Index
#
# #slicing
# #list[start:end:steps]
# print(list1[2:3])
# print(list1[-4:-3])
# print(list1[-5:-2])
#
# print(list1[2:])
# print(list1[:])
#
# print(list1[2:4])
# print(list1[-5:-3])
#
# print(list1[::-1]) #List in reverse order
#
# print("#"*100)
# #Append
# list2 = ["apple","banana","cherry","mango","papaya"]
# list2.append("abcd")
# print(list2)
#
# #insert
# list2.insert(1,"orange")
# print(list2)

# #Extend list:-mixed
# list1 = ["apple","banana","cherry","mango","papaya"]
# list2 = ["a","b","c","m","p"]
# list1.extend(list2)
# print(list1)

# #pop() #delete last and indexable element
# list3 = ["apple","banana","cherry","mango","papaya"]
# list3.pop(2)
# print(list3)
#
# #del Keyword
# del list3[1]
# print(list3)
#
# #clear
# list3.clear()
# print(list3)

# #Sorting
# list4 = [83,56,188,99]
# #--- list5 = ["h","n","j","t","r",83,56,188] #TypeError: '<' not supported between instances of 'int' and 'str'
# list5 = ["h","n","j","t","r"]
# list5.sort()
# list4.sort()
# print(list5)
# print(list4)

# #Allow different datatypes
# l1 = [1,"apple",3.14,True]
# print(type(l1))

# #copy() deep copy
# list4 = ["apple","banana","cherry","mango","papaya"]
# l1 = [1,"apple",3.14,True]
# list4=l1.copy()
# print(list4)

# # Join list using +
# l4 = ["a",34,"ab",1]
# l5 = [1,4,6,8]
# l6 = l4+l5
# print(l6)

# list10=[]
# list9=[4,6,8,9]
# for x in list9:
#     list10.append(x)
# print(list10)

# #Task -- remove duplicates from list
# #with loop method
# list9 = [1,2,2,3,55,98,65,65,13,29]
# list0 = []
# for i in list9:
#     if i not in list0:
#         list0.append(i)
#     print(list0)
#
# #With Set method
# #list8 = set(list9)
# list8 = list(set(list9))
# print(list8)

#list Comprehension
#even number
# #loop method list code
# list12=[]
# for x in range(20):
#     if x%2==0:
#         list12.append(x)
# print(list12)
#
# #compress list code
# new_list = [x for x in range(20) if x%2==0 ]
# print(new_list)
#
# new_list = [x for x in range(20) if x%2!=0 ]
# print(new_list)

# list23=[]
# for i in range(10):
#     list23.append(i+1)
# print(list23)
#
# #listname = [expression forloop ifcondition-optional]
# new_list2 = [x+1 for x in range(10) ]
# print(new_list2)

# l13=[]
# for i in range(20):
#     if i%2==0:
#         l13.append(i)
#     else:
#         l13.append("invalid")
# print(l13)

#else statement in list copmrehension
#new_list3 = [x for x in range(20) if x%2==0 else "invalid" ]
#listname = [if condition else forloop]
# new_list3 = [x if x%2==0 else "invalid" for x in range(20) ]
# print(new_list3)


#Task - remove duplicate elements from list with list comprehension method

list9 = [1,2,2,3,55,98,65,65,13,29]
list0 = []
# for i in list9:
#     if i not in list0:
#         list0.append(i)
#     print(list0)

# for i in list9:
#     if i==i:
#         print(i)
#         list0.append(i)
# print(list0)

#new_list4 = [x for x in list9 if x!=x]
# new_list4 = [i if i not in list0 else "try" for i in list9]

#new_list3 = [x if x%2==0 else "invalid" for x in range(20) ]
# new_list4 = [x if x in list0 else list0.append(x) for x in list9]
# print(list0)

new_list5 = [i for i in set(list9)]
print(new_list5)