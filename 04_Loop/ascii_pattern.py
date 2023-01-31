# for i in range(7):
#     for j in range(4):
#         if i in {0} or j in {}:
#
#             print(chr(65+i), end=" ")
#         else:
#             print(" ",end="")
#     print()

'''
  A
 A B
A B
 B C
  C
   D

'''

for i in range(7):
    for j in range(5,i,-1):
        i=j-i
        if i>3:
            print(chr(65),end=" ")



# for i in range(9):
#     for j in range(5):
#         if (i==0 and j==4) or (i==1 and j==2) or (i==2 and j==1):
#             print(chr(65),end="")
#         if (i==1 and j==3) or (i==2 and j==2) or (i==3 and j==2):
#             print(chr(66),end="")
#         if (i==2 and j==3) or (i==3 and j==3):
#             print(chr(67),end="")
#         if (i==4 and j==3):
#             print(chr(67),end="")
#         if (i==3 and j==4) or (i==4 and j==4):
#             print(chr(68),end="")
#         else:
#             print(" ",end="")
#     print()