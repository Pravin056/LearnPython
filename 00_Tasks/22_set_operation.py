'''
22.Python Program to Illustrate Different Set Operations
(update,add,issubset,isdisjoin,intersection,union etc)
'''

set1={"one","two","three"}
set2={"five","six","seven","eight"}
print(set1,type(set1))

set1.update("four")
print("Updtae",set1)

set1.add("five")
print("Add",set1)

print("isSubset",set1.issubset(set2))
print("isdisjoin",set1.isdisjoint(set2))
print("issuperset",set1.issuperset(set2))

print("intersection",set1.intersection(set2))
print("intersection_update",set1.intersection_update(set2))
print("union",set1.union(set2))

c = set1.copy()
print(c)

print("difference",set1.difference(set2))
print("difference_update",set1.difference_update(set2))

print("discard",set1.discard("one"))

r = set2.remove("seven")
print("remove",r)

print("symmetric_difference",set1.symmetric_difference(set2))
print("symmetric_difference_update",set1.symmetric_difference_update(set2))
print("pop",set2.pop())
print("clear",set2.clear())
