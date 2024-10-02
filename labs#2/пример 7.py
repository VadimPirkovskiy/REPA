import math
x = float(input('ввдеите x  : '))
y = float(input('введите y : '))
z = eval(input('введите z  : '))
s = (5*math.atan(x)) - (1/4)*math.acos(x) *((x + 3 * abs(x - y)+x**2)/(abs(x - y)*z + x**2))
print('ответ : ', round(s,3))