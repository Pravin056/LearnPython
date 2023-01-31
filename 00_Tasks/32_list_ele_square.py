'''n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = lcm(n1, n2)
32.Given a Python list of numbers. Turn every item of a list into its square Given:
List = [1, 2, 3, 4, 5, 6, 7]
'''

List = [1, 2, 3, 4, 5, 6, 7]
List2 = []
for i in List:
    s = i*i
    List2.append(s)
print(List2)