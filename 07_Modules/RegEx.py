'''
Source : https://www.w3schools.com/python/python_regex.asp

A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
RegEx can be used to check if a string contains the specified search pattern.
Python has a built-in package called "re", which can be used to work with Regular Expressions.
'''
import re

#The re module offers a set of functions that allows us to search a string for a match:
#findall - Returns a list containing all matches
txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

# search - Returns a Match object if there is a match anywhere in the string
txt = "The rain in Spain"
x = re.search("\s", txt) #\s Returns a match where the string contains a white space character
print("The first white-space character is located in position:", x.start())

# split - Returns a list where the string has been split at each match
#Split at each white-space character:
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

# Split the string only at the first occurrence:
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

# sub - Replaces one or many matches with a string
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

# The Match object has properties and methods used to retrieve information about the search, and the result:

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


'''
Metacharacters are characters with a special meaning:
Character	Description	                                            Example
[]	        A set of characters	                                    "[a-m]"
\	        Signals a special sequence (escape special characters)	"\d"
.	        Any character (except newline character)	            "he..o"
^	        Starts with	                                            "^hello"
$	        Ends with	                                            "planet$"
*	        Zero or more occurrences	                            "he.*o"
+	        One or more occurrences	                                "he.+o"
?	        Zero or one occurrences	                                "he.?o"
{}	        Exactly the specified number of occurrences	            "he.{2}o"
|	        Either or	                                            "falls|stays"
'''

'''
A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:
Character	Description	                                                                                    Example
\A	        Returns a match if the specified characters are at the beginning of the string	                "\AThe"
\b	        Returns a match where the specified characters are at the beginning or at the end of a word
            (the "r" for - "raw string")	                                                                r"\bain"
                                                                                                            r"ain\b"
\B	        Returns a match where the specified characters are present, but NOT at the beginning
            (or at the end) of a word                                                                       r"\Bain"
                                                                                                            r"ain\B"
\d	        Returns a match where the string contains digits (numbers from 0-9)	                            "\d"
\D	        Returns a match where the string DOES NOT contain digits	                                    "\D"
\s	        Returns a match where the string contains a white space character	                            "\s"
\S	        Returns a match where the string DOES NOT contain a white space character	                    "\S"
\w	        Returns a match where the string contains any word characters
            (characters from a to Z, digits from 0-9, and the underscore _ character)	                    "\w"
\W	        Returns a match where the string DOES NOT contain any word characters	                        "\W"
\Z	        Returns a match if the specified characters are at the end of the string	                    "Spain\Z"
'''

'''
A set is a set of characters inside a pair of square brackets [] with a special meaning:
Set	        Description
[arn]	    Returns a match where one of the specified characters (a, r, or n) is present
[a-n]	    Returns a match for any lower case character, alphabetically between a and n
[^arn]	    Returns a match for any character EXCEPT a, r, and n
[0123]	    Returns a match where any of the specified digits (0, 1, 2, or 3) are present
[0-9]	    Returns a match for any digit between 0 and 9
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case
[+]	        In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for
            any + character in the string
'''
