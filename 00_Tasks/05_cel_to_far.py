'''
5.Python Program to Convert Celsius To Fahrenheit .
'''

intro = '''
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
°° Celsius to Fahrenheit Converter °°
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
print(intro)

cel = float(input("Enter Celsius: "))
far = (cel*9/5)+32
print("%0.2f Celsius is %0.2f fahrenheit"%(cel,far))