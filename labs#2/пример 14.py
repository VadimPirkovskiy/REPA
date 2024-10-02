import math
x = eval(input('введите x : '))
y = float(input('введите y : '))
z = eval(input('введите z : '))
s = ((y **(x + 1)) / (((abs(y-2))**(1/3)) + 3)) + ((x + (y / 2)) / (2 * abs(x + y)))*(x + 1)**(-1/math.sin(z))
print('ОТВЕТ : ' , round(s,4))