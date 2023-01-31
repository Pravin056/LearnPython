import os
def toolIntro():
    a = '''
    🅱🆄🅻🅺 🅵🅸🅻🅴 🆁🅴🅽🅰🅼🅴🆁
    Hi, This tool help you to rename bunch of files at once!
    01. Enter Directory in which you want to change the name
    02. Select option to perform operation
        Enter 1 - Rename full name of files
        Enter 2 - Add serial number to files
        Enter 3 - Add extension into the files name
    '''
    print(a)
toolIntro()
filePath = input("Enter Directory :")
if not filePath.endswith("/"):
    filePath = filePath+"/"
def validateDir(dirName):
    if os.path.isdir(dirName) and os.path.exists(dirName):
        print("[info]:Validated Directory: ",dirName)
    else:
        print("[Error]:you have entered wrong path or directory is not exist!")

def fileList(filePath):
    filesP = os.walk(filePath)
    fileP = []
    for r,d,f in filesP:
        fileP.append(f)
    fileP = fileP[0]
    fileP2 = []
    for i in fileP:
        if i.startswith("."): #ignore hidden files
            continue
        else:
            fileP2.append(i)
    return fileP2

def ignrExt(fname):
    fnamen = fname.split(".")[0]
    return fnamen
def addE(fExt):
    fExt1 = fExt.split(".")[1]
    return fExt1
def addExt():
    ext = input("Enter Extention: ")
    list2 = [i for i in fileList(filePath)]
    for i in list2:
        os.renames(filePath+i,filePath+ignrExt(i)+ext+"."+addE(i))
    print("[info]:Extention",ext,"Added Successfully!")

def addSr():
    list2 = [i for i in fileList(filePath)]
    count = [i for i in range(len(list2))]
    for j,k in zip(list2,count): #zip returns an iterator of tuples
            os.renames(filePath+j,filePath+str(k)+"_"+ignrExt(j)+"."+addE(j))
    print("[info]:Serial numbers added successfully!")

def renamefullname():
    newname = input("Enter new name: ")
    list3 = [i for i in fileList(filePath)]
    count = [i for i in range(len(list3))]
    for j,k in zip(list3,count):
        os.renames(filePath + j, filePath + newname + "_" + str(k) + "." + addE(j))
    print("[info]:File(s) renamed successfully!")

def main():
    validateDir(filePath)
    fileList(filePath)
    userInput = int(input("Select Option: "))
    if userInput==1:
        renamefullname()
    elif userInput==2:
        addSr()
    elif userInput==3:
        addExt()
    else:
        print("[Error]:Please select '1' , '2' or '3'")

#Fun start here!
main()