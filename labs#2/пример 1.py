import math
x = float(input('введите x : '))
y = float(input('введите y : '))
z = eval(input('введите z : '))
a = (2 * math.cos(x-2/3))/(1/2 + math.sin(y)**2)*(1 + (( z **2 )/( 3 - z **2 / 5 )))
print('ответ : ',round(a,6))
