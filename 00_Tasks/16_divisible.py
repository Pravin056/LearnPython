'''
16.Python Program to Find Numbers Divisible by Another Number.
'''

def divisible(s,e):
    if s%e==0:
        print(e,"is divisible of",s)
    else:
        print(e, "is not divisible of", s)

start = int(input("Start Number: "))
end = int(input("End Number: "))

divisible(start,end)