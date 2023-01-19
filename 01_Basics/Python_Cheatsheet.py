'''
Python CheatSheet
Basics
Basic syntax from the python programming language
Showing Output To User
The print function is used to display or print output as follows
https://www.codewithharry.com/blogpost/python-cheatsheet/
'''
print("Content that you wanna print on screen")

#we can display the content present in object using prit function as follows:-
var1 = "Pravin"
print("Hi my name is: ",var1)

'''
Taking Input From the User
The input function is used to take input as string or character from the user as follows:
'''
var1 = input("Enter your name: ")
print("My name is: ", var1)

'''
To take input in form of other datatypes we need to typecaste them as follows:-
'''
#To take input as an integer:-
var1=int(input("enter the integer value"))
print(var1)

#To take input as an float:-
var1=float(input("enter the float value"))
print(var1)

'''
range Function
range function returns a sequence of numbers, eg, numbers starting from 0 to n-1 for range(0, n)
'''
#range
range(int_start_value,int_stop_value,int_step_value)

'''
Here the start value and step value are by default 1 if not mentioned by the programmer.
but int_stop_value is the compulsory parameter in range function
example-
Display all even numbers between 1 to 100
'''
for i in range(0,101,2):
       print(i)

'''
Comments
Comments are used to make the code more understandable for programmers, and they are not executed by compiler or interpreter.
'''
# This is a single line comment
'''This is a
multi-line
comment'''

'''
Escape Sequence
An escape sequence is a sequence of characters; it doesn't represent itself
(but is translated into another character) when used inside string literal or character.
Some of the escape sequence characters are as follows:
'''
#Newline Character
print("\n")
#backslash
print("\\")
#Single Quote
print("\'")
#Tab
print("\t")
#Backspace
print("\b")
#Octal value
print("\ooo")
#Hex value
print("\xhh")
#Carriage Return
'''Carriage return or \r will just work as you have shifted your cursor to the beginning of the string or line.'''
print("\r")

'''
Strings
Python string is a sequence of characters, and each character can be individually accessed using its index.
You can create Strings by enclosing text in both forms of quotes - single quotes or double quotes.
'''
variable_name = "String Data"
#i.e.
str="Pravin"
print("string is ",str)

#Indexing
'''
Indexing
The position of every character placed in the string starts from 0th position ans step by step it ends at length-1 position
'''
#Slicing
'''
Slicing
Slicing refers to obtaining a sub-string from the given string.
The following code will include index 1, 2, 3, and 4 for the variable named var_name
Slicing of the string can be obtained by the following syntax-
'''
#string_var[int_start_value:int_stop_value:int_step_value]
#here start and step value are considered 0 and 1 respectively if not mentioned by the programmmer
var_name = "Pravin"
new_var = var_name[1 : 5]
print(var_name,new_var)

'''
isalnum() method
Returns True if all the characters in the string are alphanumeric, else False

isalpha() method
Returns True if all the characters in the string are alphabets

isdecimal() method
Returns True if all the characters in the string are decimals

isdigit() method
Returns True if all the characters in the string are digits

islower() method
Returns True if all characters in the string are lower case

isspace() method
Returns True if all characters in the string are whitespaces

isupper() method
Returns True if all characters in the string are upper case
'''
string_variable=" Pravin "
string_variable.isalnum()
string_variable.isalpha()
string_variable.isdecimal()
string_variable.isdigit()
string_variable.islower()
string_variable.isspace()
string_variable.isupper()

'''
lower() method
Converts a string into lower case equivalent

upper() method
Converts a string into upper case equivalent

strip() method
It removes leading and trailing spaces in the string
'''
string_variable.lower()
string_variable.upper()
string_variable.strip()

