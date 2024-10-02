import math
x = float(input('введите x : '))
y = eval(input('введите y : '))
z = eval(input('введите z : '))
s = ((math.pow(9 + (x - y)**2 , 1/3)) / (x**2 + y **2 + 2)) - math.exp(abs(x - y))*math.tan(z)**3
print('ответ : ',round(s,5))
