'''
Python has several functions for creating, reading, updating, and deleting files.

The key function for working with files in Python is the open() function.
The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:
"r" - Read      - Default value. Opens a file for reading, error if the file does not exist
"a" - Append    - Opens a file for appending, creates the file if it does not exist
"w" - Write     - Opens a file for writing, creates the file if it does not exist
"x" - Create    - Creates the specified file, returns an error if the file exists

"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
'''

#below mentioned both statements are same.
f = open("GoldenTouch.txt")
f = open("GoldenTouch.txt", "rt")
#Because "r" for read, and "t" for text are the default values, you do not need to specify them.

print(f)            #Output:- <_io.TextIOWrapper name='GoldenTouch.txt' mode='rt' encoding='UTF-8'>
print(f.readline()) #Read first line
print(f.readline()) #Read Second/next line

#this loop read all lines
for x in f:
  print(x)

#Close file
f.close()

#Write to an Existing File
#"a" - Append - will append to the end of the file
f = open("GoldenTouch02.txt", "a")
f.write("The Midas Touch!")
f.close()
f = open("GoldenTouch02.txt","r")
print(f.read())


#"w" - Write - will overwrite any existing content
f = open("GoldenTouch02.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
f = open("GoldenTouch02.txt", "r")
print(f.read())


#Create a New File and append or write new content in it.
#f = open("GoldenTouch03.txt", "x") # it will omit error if file is already exists
f = open("GoldenTouch03.txt", "w") #cerate new file or overwrite existing file
f = open("GoldenTouch03.txt", "a") #append data in axisting file
f.write("Created new file and append this line!")
f.close()
f = open("GoldenTouch03.txt", "r") #Open file as Read-Only
print(f.read()) #read data from file


#Delete file in Python ------------------------------------------------------------
#To delete a file, you must import the OS module, and run its os.remove() function:

import os
os.remove("GoldenTouch03.txt")

#Check file is exist or not. if exists the delete the file
if os.path.exists("GoldenTouch03.txt"):
  os.remove("GoldenTouch03.txt")
else:
  print("The file does not exist")

#Delete Folder
os.rmdir("myfolder")