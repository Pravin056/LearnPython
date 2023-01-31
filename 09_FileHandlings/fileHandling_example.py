#REad bit and byte
#Learn what is UTF-8

f=open("AboutMyself.txt","r")
# #print(f)
# print(f.readline())
# print(f.readline())

f1=open('abc','a')
f1.write("something\t")
f1.write("people\t")

f1=open('abc','a')
f1.write("very smart\n")

for data in f:
    f1.write(data)

