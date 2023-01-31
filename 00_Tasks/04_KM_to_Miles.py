'''
4.Python Program to Convert Kilometers to Miles .
'''

intro='''
###################################
## KILOMETRE TO MILE CONVERTER  ##
#################################
'''
print(intro)

KM = float(input("Enter KiloMetre: "))
miles = KM/1.609

#print(KM,"Kilometre is ",miles,"Miles")
print("%0.2f Kilometre is %0.4f Miles"%(KM,miles)) #you can control floating points with "%0.3f" %(varname)