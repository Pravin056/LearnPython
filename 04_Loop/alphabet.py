# for i in range(65,75):
#     for j in range(65,75):
#         print(chr(i),end="")
#     print()
#----------------------------------------------
# for i in range(5):
#     for j in range(5):
#         print(chr(65+i),end="")
#     print()
#------------------
#print(chr(80,82,65,86,73,78))
#print(chr(80),chr(82),chr(65),chr(86),chr(73),chr(78))

# for i in range(5):
#     for j in range(5-i):
#         print(chr(65+i),end=" ")
#     print()

# for i in range(5):
#     for j in range(5-i):
#         print(chr(69-i),end=" ")
#     print()

for i in range(6):
    for j in range(1):
        #if i==80 or i==82 or i==65 or i==86 or i==73 or i==78:
        a=[80,82,65,86,73,78]
        print(chr(a[i]),end=" ")
    print(end="")

'''
A 
B C 
C D E 
D E F G 
E F G H I
'''

# for i in range(5):
#     for j in range(i+1):
#         print(chr(65+i+j),end=" ")
#     print()

'''
E F G H I 
D E F G 
C D E 
B C 
A
'''
# for i in range(5):
#     for j in range(5-i):
#         print(chr(69-i+j),end=" ")
#     print()
#----------------------------------------------------
# for i in range(5,0,-1):
#     for j in range(i):
#         print(chr(64+i+j),end=" ")
#     print()