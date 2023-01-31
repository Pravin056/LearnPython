'''
20.Python Program to Remove Punctuations From a String.
'''

str5 = input("Enter String: ")
p = ['.','"',"'",'?',':',';','!','(',')','[',']','...','-','_','/','@','{','}','*']
r = ""
for i in str5:
    if i not in p:
        r += i
print(r)