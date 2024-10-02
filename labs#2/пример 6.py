import math
x = eval(input("ввведите x : "))
y = float(input("введите y : "))
z = float(input("введите z : "))
s =(math.sqrt((x**(1./3.))+(x**(y+2)))*(10**(1/2)))*((math.asinh(z)**2) - abs(x-y))
print('ответ : ' ,  round(s , 4 ))