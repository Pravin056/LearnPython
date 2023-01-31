'''

2.Python Program to Calculate the Area of a Triangle

'''

#formula :- area = 1/2 * base * height.

base = int(input("Base : "))
height = int(input("height : "))
area = 1/2*base*height

#k = base - 1
for i in range(height):
    for j in range(base):
        print(end=" ")
    base = base - 1
    for j in range(i + 1):
        print("* ", end="")
    print("")
print("Area of triangle is",area)