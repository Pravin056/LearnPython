#Import - Module
#Install - Package

'''
Custom Module for Calculater
Python - Collection od Packages
Package - Collection of Modules
Module - Collection of Functions
'''

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

def facto(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

def febo(x):
    for i in range(x+1):
        if x <= 1:
            return x
        else:
            return febo(x-1)+febo(x-2)

def febo2(n):
    flist = [febo(n) for n in range(n)]
    return flist

def oddeve(n):
    if n == 0:
        print("Number is Zero")
    elif n % 2 == 0:
        print(n,"Number is Even")
    else:
        print(n,"Number is Odd")

def palindrome(string):
    stringrev=string[::-1]
    if string==stringrev:
        print(string+" is Palindrome")
    else:
        print(string+" is not Palindrome")

def primeN(num):
    f = False
    for i in range(2, num):
        if (num % i) == 0:
            f = True
            break
    if f:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")