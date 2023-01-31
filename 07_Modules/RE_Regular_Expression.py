import re
#MATCH CHARACTER
#Check if the string starts with "The" and ends with "Spain"

# txt = "My students of pyt59 batch"
# x = re.search("^My.*batch$",txt) #MetaCharacters
#
# if x:
#     print("YES!, We have match!")
# else:
#     print("No Match")

# txt = "India is great country"
# #Find all lower case character alphabetically between "a" and "m"
# x = re.findall("[a-m]",txt)
# print(x)


# txt = "my Degree marks is 78%"
# #Find all digit characters
# x = re.findall("\d",txt)
# print(x)

# txt = "hello planet"
# #Search for sequence that starts with "pal", followed by two (any) character and "t"
# x = re.findall("pal..t",txt)
# print(x)

# txt = "hello planet"
# #Search for sequence that starts with "he", followed by two (any) character and an "o"
# x = re.findall("he.{2}o",txt)
# print(x)

# txt = "The rain in Spain falls mainly in the plain"
# #check if string contains either "falls" or "stays"
# x = re.findall("falls|the",txt)
# print(x)
#
# if x:
#     print("Yes, there is at least one match!")
# else:
#     print("No match")


# #Special Sequence
# txt = "The moon"
# #Check if string starts with "The"
# x = re.findall("\AThe",txt) #\A for starting character
# print(x)
#
# if x:
#     print("Yes, there is at least one match!")
# else:
#     print("No match")

# #Set
# txt = "The rain in Spain"
#
# #Check if the string has any a,r,or characters
# x = re.findall("[arn]",txt)
# print(x)
#
# if x:
#     print("Yes, there is at least one match!")
# else:
#     print("No match")

# #Set
# txt = "The rain in Spain"
#
# #Check if the string has any characters other than a,r or n
# x = re.findall("[^arn]",txt)
# print(x)
#
# if x:
#     print("Yes, there is at least one match!")
# else:
#     print("No match")


# #digit
# txt = "The rain in Spain 123"
#
# #Check if the specified digits are available in string
# x = re.findall("[0123]",txt)
# print(x)
#
# if x:
#     print("Yes, there is at least one match!")
# else:
#     print("No match")

# #Find Time
# txt = "8 times before 11:30 AM"
# #check is string have any two digit number from 00 to 59
# x = re.findall("[0-5][0-9]",txt)
# print(x)
#
# if x:
#     print("Yes, there is at least one match!")
# else:
#     print("No match")

#Find letters
# txt = "8 times before 11:30 AM"
# #check if string has any charater from a to z lower cad and A to Z upper case
# x = re.findall("[a-zA-Z]",txt)
# print(x)
#
# if x:
#     print("Yes, there is at least one match!")
# else:
#     print("No match")

# txt = "8 times before 11:30 AM +"
# #check if string has any + character
# x = re.findall("[+]",txt)
# print(x)
#
# if x:
#     print("Yes, there is at least one match!")
# else:
#     print("No match")

# ##SEARCH
# txt = "The rain in spain"
# x = re.search("spain",txt)
# print(x)
#
# #SPLIT
# #Split the string at every white-space character
# txt = "The rain in spain"
# x = re.split("\s",txt)
# print(x)
#
# #Split the string at first two white-space character
# txt = "The rain in spain"
# x = re.split("\s",txt,2)
# print(x)

# #Replace all white-space character with digit 9
# txt = "The rain in spain"
# x = re.sub("\s","9",txt)
# print(x)

# #Replace first white-space character with digit 9
# txt = "The rain in spain"
# x = re.sub("\s","9",txt,1)
# print(x)

# .span() returns a tuple containing the start-, and end positions of the match.
#The regular expression looks for any words that starts with an upper case "S":
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

# .string returns the string passed into the function
#Print the string passed into the function:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

# .group() returns the part of the string where there was a match
#The regular expression looks for any words that starts with an upper case "S":
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())

