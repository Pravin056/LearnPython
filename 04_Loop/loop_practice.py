'''
Exercise 1: Print the following pattern
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''

# for i in range(6):
#     for j in range(i):
#         print(j+1, end=" ")
#     print(" ")
#


'''
Exercise 2: Calculate the sum of all numbers from 1 to a given number
For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)
'''
# s=0
# a=int(input("Enter Number: "))
#
# for i in range(a+1):
#     s+=i
# print("Sum is: ",s)
#


'''
Exercise 3: Write a program to print multiplication table of a given number
'''
# a=int(input("Enter Number: "))
# for i in range(1,11):
#     p=a*i
#     print(p)


'''
Exercise 4: Display numbers from a list using loop
Write a program to display only those numbers from a list that satisfy the following conditions

    The number must be divisible by five
    If the number is greater than 150, then skip it and move to the next number
    If the number is greater than 500, then stop the loop

numbers = [12, 75, 150, 180, 145, 525, 50]
'''

# numbers = [12, 75, 150, 180, 145, 525, 50]
#
# for i in numbers:
#     if i>500:
#         break
#     elif i>150:
#         continue
#     elif i%5==0:
#         print(i)


'''
Exercise 5: Count the total number of digits in a number
Write a program to count the total number of digits in a number using a while loop.
For example, the number is 75869, so the output should be 5.
'''
# counter=0
# num=75869
# while num!= 0:
#     num=num//10
#     counter+=1
# print(counter)


'''
Exercise 6:Print the following pattern
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
'''
# for i in range(5):
#     for j in range(5-i,0,-1):
#         print(j,end=' ')
#     print(" ")

'''
Exercise 7: Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]
'''
# list1 = [10, 20, 30, 40, 50]
# l = len(list1)-1
# for i in range(l,-1,-1):
#     print(list1[i])
#
# print("^"*100)
#
# new_list=reversed(list1)
# for i in new_list:
#     print(i)

'''
Exercise 8: Display numbers from -10 to -1 using for loop
'''
# for i in range(-10,0,1):
#     print(i)

'''
Exercise 9: Use else block to display a message “Done” after successful execution of for loop
for i in range(5):
    print(i)
'''

# for i in range(5):
#     print(i)
# print("Done!")

'''
Exercise 10: Write a program to display all prime numbers within a range
Note: A Prime Number is a number that cannot be made by multiplying other whole numbers. A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers

Examples:

    6 is not a prime number because it can be made by 2×3 = 6
    37 is a prime number because no other whole numbers multiply together to make it.
# range
start = 25
end = 50
'''
# # range
# start = 25
# end = 50
#
# for i in range(start,end+1):
#     if i > 1:  #all prime numbers are greater than 1
#         for j in range(2,i):
#             if (i % j) == 0: #check for factors - Prime number
#                 break
#         else:
#             print(i)

'''
Exercise 11 : Print String in pattern
i.e string is "Pravin" print it in mentioned pattern
P  
P r  
P r a  
P r a v  
P r a v i  
P r a v i n 
'''
# name="Pravin"
# l=len(name)
#
# for i in range(l):
#     for j in range(i+1):
#         print(name[j], end=" ")
#
#     print(" ")


'''
Exercise 12: Display Fibonacci series up to 10 terms
The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it. The first two numbers are 0 and 1.
For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34.

Expected output:
Fibonacci sequence:
0  1  1  2  3  5  8  13  21  34
'''
# num1=0
# num2=1
#
# for i in range(10):
#     print(num1, end=" ")
#     res = num1 + num2
#     num1 = num2
#     num2 = res

'''
Exercise 13: Find the factorial of a given number
The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1
For example: calculate the factorial of 5
5! = 5 × 4 × 3 × 2 × 1 = 120
'''

# fact=1
# for i in range(1,6):
#     fact=fact*i
# print(fact)

#------------------------------------

# num=5
# fact=1
# for i in range(1,num+1):
#     fact = fact*i
# print(fact)

'''
Exercise 14: Reverse a given integer number
'''
# num = 76542
# print(num)
# rev_num = 0
# while num > 0:
#     rem = num % 10
#     rev_num = (rev_num * 10) + rem
#     num = num // 10
# print(rev_num)