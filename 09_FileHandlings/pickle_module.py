import pickle
f=open("AboutMyself.txt",'wb')
dct = {"name":"Ravi", "age":23, "Gender":"M","marks":75}
pickle.dump(dct,f)
f.close()

#How to run Binary files
f = open("AboutMyself.txt","rb")
d = pickle.load(f)
print(d)
f.close()

