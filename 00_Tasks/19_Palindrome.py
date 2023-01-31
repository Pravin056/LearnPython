'''
19.Python Program to Check Whether a String is Palindrome or Not.
'''

def palindrome(string):
    stringrev=string[::-1]
    if string==stringrev:
        print(string+" is Palindrome")
    else:
        print(string+" is not Palindrome")

word = input("Enter Text: ")
palindrome(word)