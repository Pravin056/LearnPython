# def pyt61():
#     return 1 #Function only return single return value
#     return 2 #ignore by function
#     return 3 #ignore by function
# x = pyt61()
# print(x,type(x))

# def pyt61():
#     yield 1
#     yield 2
#     yield 3
# x = pyt61()
# print(x,type(x))
# print(x.__next__()) #"__" is called Dunder
# print(x.__next__())
# print(x.__next__())
# #print(x.__next__()) #StopIteration

'''
Generator creates own iterator
'''
# def num(a,b):
#     yield a + b
#     yield a - b
#     yield a * b
#     yield a ** b
#     yield a / b
#     yield a // b
#
# y = num(5,4)
# print("sum",y.__next__())
# print("sub",y.__next__())
# print("mult",y.__next__())
# print("expo",y.__next__())
# print("div",y.__next__())
# print("floord",y.__next__())

# #in factorial case retur and yield occupied same memory so we can continue with return instead if yield
# def fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact = fact*i
#     return fact
#     #yield fact
#
# f = fact(5)
# #print(f.__next__())
# print(f)

#use "yield" - generator when loop returns series as value.

def febo(x):
    for i in range(x+1):
        if x <= 1:
            return x
        else:
            return febo(x-1)+febo(x-2)

def febo2(n):
    for n in range(n):
        yield febo(n)


fb = febo2(10)

print(fb.__next__())
print(fb.__next__())
print(fb.__next__())
print(fb.__next__())
print(fb.__next__())
print(fb.__next__())
print(fb.__next__())
