n = int(input("Enter row count: "))
s = input("Enter Sign : ")
for i in range(1,n+1):
    for j in range(1,n+1):
        if i in {1,n} or j in {1,n}:
            print(s,end="  ")
        else:
            print(" ",end="  ")
    print()