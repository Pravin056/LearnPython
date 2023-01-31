def febo(rng):
    n1 = 0
    n2 = 1
    for i in range(rng):
        print(n1,end=" ")
        n3 = n1 + n2
        n1 = n2
        n2 = n3
rng=int(input("Enter Number: "))
febo(rng)

def febo2(x):
    for i in range(x+1):
        if x <= 1:
            return x
        else:
            return febo2(x-1)+febo2(x-2)

n = int(input("Enter Number: "))
flist=[febo2(n) for n in range(n)]
print(flist)
    
