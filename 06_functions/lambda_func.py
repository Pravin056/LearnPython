'''
source : https://www.freecodecamp.org/news/python-lambda-function-explained/

What is a Lambda Function?
Lambda functions are similar to user-defined functions but without a name.
They're commonly referred to as anonymous functions.

Lambda functions are efficient whenever you want to create a function that will only contain simple expressions.
expressions that are usually a single line of a statement. They're also useful when you want to use the function once.
'''

#How to Define a Lambda Function:

#lambda argument(s) : expression
'''
01. "lambda" is a keyword in Python for defining the anonymous function.
02. "argument(s)" is a placeholder, that is a variable that will be used to hold the value you want to pass into
    the function expression. A lambda function can have multiple variables depending on what you want to achieve.
03. "expression" is the code you want to execute in the lambda function.
'''

#No return keyword
'''
Notice that the anonymous function does not have a return keyword. This is because the anonymous function will
automatically return the result of the expression in the function once it is executed.
'''

#Function vs lambda Example:
#Assume I want to write a function that returns twice the number I pass it.

def twiceF(x):
  return x * 2

print(twiceF(5))

#---------------------------

twiceL = lambda x: x * 2
print(twiceL(5))

#you can directly call the lambda function without defining function name. that's why its called "Anonymous Function"
twiceL2 = (lambda x : x * 2)(5)
print(twiceL2)

#Use Caces of Lambda
'''
Filter()
When you want to focus on specific values in an iterable, you can use the filter function.
The following is the syntax of a filter function:

filter(function, iterable)

As you can see, a filter function requires another function that contains the expression or
operations that will be performed on the iterable.
'''
#Example :
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filter(lambda x: x % 2 == 0, list1)
#Output:
# <filter at 0x1e3f212ad60> #The result is always filter object so I will need to convert it to list using list()
list2 = list(filter(lambda x: x % 2 == 0, list1))
print(list2)


'''
Map()
You use the map() function whenever you want to modify every value in an iterable.

map(function, iterable)
'''
#Example:
#If you want to raise all values in the below list to the power of 2
list3 = [2, 3, 4, 5]
list4 = list(map(lambda x: pow(x, 2), list3))
print(list4)
