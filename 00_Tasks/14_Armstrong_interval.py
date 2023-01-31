'''
14.Python Program to Find Armstrong Number in an Interval.
'''

def armint(s,e):
    for num in range(s,e+1):
        lenn = len(str(num))
        sum = 0
        temp = num
        while temp > 0:
            dg = temp % 10
            sum += dg**lenn
            temp //= 10
        if sum==num:
            print(num,end=" ")

start = int(input("Start Number: "))
end = int(input("End Number: "))

armint(start,end)
