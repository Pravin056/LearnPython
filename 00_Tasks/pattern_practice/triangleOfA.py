
s = input("Enter Sign/Letter: ")
n = int(input("Enter Row count: "))
for i in range(1,n+1):
    for k in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(1,i+1):
        if i and j in {1} or i in {n} or j in {i}:
            print(" ", s,end=" ")
        else:
            print(" ",end="   ")
    print()