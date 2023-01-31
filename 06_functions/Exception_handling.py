#---------- NameError: ---------------------
try:
    print(x)
except NameError:
    print("Value of x is not assign")

#------------ ValueError: --------------------
try:
    a = int(input("Enter Number: "))
except ValueError:
    print("Please enter number")

#------------ TypeError: ----------------------
try:
    print(1+"ab")
except TypeError:
    print("add operation not supported with number and text")

#------------ ValueError: --------------------
try:
    s=float(input("Enter Number: "))
except ValueError:
    print("Please enter number")

#-------- ZeroDivisionError: ------------------
a=10
b=0
try:
    print(a/b)
except ZeroDivisionError:
    print("value of b is",b,"not able divide",a,"with",b)

#----------- IndentationError: -------------------

p=2
try:
            print(p)
except IndentationError:
    print("Please check spacing")


#------- RecursionError: -------------------------------
def abc():
    print("Recursive")
    abc()
try:
    abc()
except RecursionError:
    print("Error: Function have recursive operations")

#--------------- finally ----------------------------
try:
    a=10
    b=0
    print("Open")
    print(a/b)
except ZeroDivisionError:
    print("you cant use zero for division")
finally:
    print("close")

#----------- IndexError: ---------------------------
try:
    s=[1,2,3,4,5]
    print(s[6])
except IndexError:
    print("Index out of range list length is",len(s))
