'''
Dynamically make below pattern

          1
        1   2
      1       3
    1           4
  1   2   3   4   5

'''

n = int(input("Enter Row count: "))
for i in range(1,n+1):
    for k in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(1,i+1):
        #if i==1 or j==1 or i==n or j==i or j==i+1:
        # if i==3:
        #     continue
        if i and j in {1} or i in {n} or j in {i}:
            print(" ", j,end=" ")
        else:
            print(" ",end="   ")
    print()