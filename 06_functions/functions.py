# #def function_name(): #How to create Function in Python
# #   Statement
# #   return() # we can use return once in def
#
# #def add(a): #TypeError: add() takes 1 positional argument but 2 were given
# def add(a,b):
#     return(a+b)
# #print(add(20)) #TypeError: add() missing 1 required positional argument: 'b'
# print(add(20,30))
#
# '''
# Function TypeError
# Default Argument : when you have 1 argument and 2 values
# Require Argument : When you have 2 arguments abd 1 value
# '''
#
# #With Parameter without return type
# def add1(a,b):
#     print(a+b)
# add(20,30)
#
# #With Parameter and return type
# def add2(a,b):
#     return(a+b)
# print(add(20,30))
#
# #Without parameter and return type
# a=int(input("Enter Number: "))
# b=int(input("Enter Number: "))
# def add3():
#     print(a+b)
# add3()
#
# #Without parameter with return type
# a=int(input("Enter Number: "))
# b=int(input("Enter Number: "))
# def add4():
#     return(a+b)
# print(add4())

# #Function Parameter and values
# def myfun(a):
#     print(a)
# myfun("Pytho",3000,"Thane") #TypeError: myfun() takes 1 positional argument but 3 were given

'''
*arg -- #Variable length argument / parameter. defines unlimited argument count.
**kwarg -- #"**" use to define Key = Argument.

difference
*arg vs **kwarg
arg use to define argument only, kwarg is use to define key and argument.
arg execute tuple output and kwarg omits dictionary output.
we use "*" notation (wildcard) for arg and "**" for kwarg

'''
# def myfun1(*a): #Variable length argument / parameter. defines unlimited argument count.
#     print(a)
# myfun1("Pytho",30000,"Thane")


# def myfun2(**a): #"**" use to define Key = Argument.
#     print(a)
# myfun2(course = "Python",fee = 30000,city = "Thane",contact = 987654321) #output Dictionary

def myfun2(**a): #"**" use to define Key = Argument.
    print(a)
myfun2(course = "Python",fee = 30000,city = "Thane",contact = 987654321) #output Dictionary
# #------------------------------------------------

