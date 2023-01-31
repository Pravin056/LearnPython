from time import *
c=time()
print(c)

d=gmtime()
print(d)

f=localtime()
print(f)

g=asctime()
print(g)

g=asctime(d) #We can pass attribute in "asctime()"
print(g)

h=ctime() #"ctime()" not allowed attributes | TypeError: 'time.struct_time' object cannot be interpreted as an integer
print(h)

j=sleep(10) #pause process for time being
print("hello",j)