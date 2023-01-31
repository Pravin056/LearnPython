'''
23.Python Program to Count the Number of Each Vowel.
'''

text1 = input("Enter Text: ")
text1 = text1.casefold() #caseless comparisions
vow = "aeiou"
vow_count = {x:sum([1 for c in text1 if c == x]) for x in vow}
print(vow_count)