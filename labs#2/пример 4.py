import math
x = eval(input('введите x : '))
y = float(input('введите y : '))
z = eval(input('введите z : '))
s = (abs(math.cos(x)-math.cos(y))**(1 + 2*math.sin(y)**2))*(1+ z + ((z**2)/2)+((z**3/3)+((z**4)/4)))
print('Результат : ' ,  round(s , 5))