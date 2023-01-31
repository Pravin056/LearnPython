# name="Quastech"
# l=len(name)
#
# for i in range(l):
#     for j in range(i+1):
#         print(name[j], end=" ")
#     print(" ")

#--------------------------------------
'''
print mentioned pattern

      *
      *
*  *  *  *  * 
      *
      *
'''

# for i in range(6):
#     for j in range (5):
#         if (i==0 and j==0) or (i==0 and j==1) or (i==0 and j==3) or (i==1 and j==4) or\
#                 (i==1 and j==0) or (i==1 and j==1) or (i==1 and j==3) or (i==1 and j==4) or \
#                 (i==3 and j==0) or (i==3 and j==1) or (i==3 and j==3) or (i==3 and j==4) or \
#                 (i==4 and j==0) or (i==4 and j==1) or (i==4 and j==3) or (i==4 and j==4):
#             print(" ",end=" ")
#         elif (i==0 and j==2) or (i==1 and j==2) or (i==3 and j==2) or (i==4 and j==2) or \
#                 (i==2 and j==0) or (i==2 and j==1) or (i==2 and j==2) or (i==2 and j==3) or (i==2 and j==4):
#             print("*",end=" ")
#     print(" ")

# for i in range(5):
#     for j in range (6):
#         if i in {0,1,3,4} and j in {2}:
#             print("*",end=" ")
#         if i in {2} and j in {0,1,3,4,2}:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

'''
Print first letter of your name P:
* * * 
*     *
* * * 
*
*
'''

# for i in range(5):
#     for j in range(5):
#         if j in {0}:
#             print("*", end=" ")
#         if j in {1,2} and i in {0}:
#             print("*", end=" ")
#         if j in {1,2} and i in {2}:
#             print("*", end=" ")
#         if j in {3} and i in {1}:
#             print("*", end=" ")
#         if j in {1,2} and i in {1}:
#             print(" ", end=" ")
#
#     print()

# # P letter
# a = input("please enter sign: ")
# for i in range(5):
#     for j in range(5):
#         if (j in {0}) or (j in {1,2} and i in {0}) or (j in {1,2} and i in {2}) or (j in {3} and i in {1}):
#             print(a, end=" ")
#         if j in {1,2} and i in {1}:
#             print(" ", end=" ")
#     print()

# # D letter
# for i in range(5):
#     for j in range(5):
#         if (j in {0}) or (j in {1,2} and i in {0}) or (j in {1,2} and i in {4}) or (j in {3} and i in {1,2,3}):
#             print("*", end=" ")
#         if j in {1,2} and i in {1,2,3}:
#             print(" ", end=" ")
#     print()

a = input("please enter sign: ")
for i in range(5):
    for j in range(5):
        if (j in {0}) or (j in {1,2} and i in {0}) or (j in {1,2} and i in {2}) or (j in {3} and i in {1}):
            print(a, end=" ")
        if j in {1,2} and i in {1}:
            print(" ", end=" ")
    print()

