# a = '''
# 	😊😊😊😊😊
# 	😊😊😊😊😊
# 	😊😊😊😊😊
# 	😊😊😊😊😊
# '''
# print(a)
#
# str = "Python is interpreted language high-level general purpose programming language"
# print(str.index("g"))
# print(str.islower())
#
# i = str[11:21]
# print(i)
#
#
# s2 = "student@123"
# print("alpha numeric",s2.isalpha())
# print("digit", s2.isdigit())
# print("hello".capitalize())
# print(s2.isalnum())
#
# #s=s2[2]="y" #TypeError: 'str' object does not support item assignment
# #print(s)
#
# #formatting
# #fruit="apple","mango","banana"
# fruit="{2} {1} {0}".format("apple","mango","banana")
# print(fruit)
#
# #we can assign variable in format method
# fruit2="{b} {a} {c}".format(a="apple",b="mango",c="banana")
# print(fruit2)
#
# str2 = "Python is an interpreted language high-level general purpose programming language"
# print("no. of string",len(str2))
# list1=str2.split(' ') #we can split string and convert in list with str.split() method
# print(list1)
# print(list1[3])
# print(len(list1))
#
# print(str2.title())
#
# #Type Casting of list to string with join method
# list2=["apple","mango","banana"]
# print(type(list2))
# str12 = ",".join(list2)
# print(str12,type(str12))


# #Task -- Remove vowels from string
# str4 = "Welcome to quastech"
# v = ['a','A','e','E','i','I','o','O','u','U']
# r = ""
# for i in str4:
#     if i not in v:
#         r += i
# print(r)
#
#Task02
# str5 = input("Enter String: ")
# v = ['a','A','e','E','i','I','o','O','u','U']
# r = ""
# for i in str5:
#     if i not in v:
#         r += i
# print(r)
#
# #Task03
# str6 = input("Enter Username: ")
# v = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=',',','<','.','>','/','?',';',':','"',"'",'[',']','{','}','\\','|']
# r = ""
# for i in str6:
#     if i in v:
#         r = "Do not use Special Character in username "+str6
# print(r)

#Task04
string = input("Enter String:")
index = int(input("Enter Number: "))
list1=list(string)
list1.pop(index-1)
new_string="".join(list1)
print("New String",new_string)




