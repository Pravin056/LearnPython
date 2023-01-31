import random
#randrange
a=random.randrange(1,6)
print(a)
#---------------------------
#random
b=random.random() #float
print(b)
#---------------------------
#randint
c=random.randint(2,6)
print(c)
#---------------------------
#uniform
d=random.uniform(31,35) #float
print(d)
#---------------------------
#choice
p=["c++","python","java","c#",".net"]
g=random.choice(p)
print(g)
#---------------------------
#tuple
t=(34,45,67,89)
h=random.choice(t)
print(h)
#---------------------------
#shuffle
random.shuffle(p)
print(p)

# random.shuffle(t) #TypeError: 'tuple' object does not support item assignment
# print(t) #becaue tuple in immutable we do not change anything in tuple