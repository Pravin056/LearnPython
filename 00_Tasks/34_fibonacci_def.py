def febo(x):
    for i in range(x+1):
        if x <= 1:
            return x
        else:
            return febo(x-1)+febo(x-2)

n = int(input("Enter Number: "))
flist=[febo(n) for n in range(n)]
print(flist)