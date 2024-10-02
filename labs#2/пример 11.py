import math
x = float(input('введите x : '))
y = float(input('введите y : '))
z = float(input('введите z : '))
s = y**((abs(x))**(1/3)) + (math.cos(y)**3)*(((abs(x - y))*(1 + ((math.sin(z)**2)/math.sqrt(x + y))))/(math.exp(abs(x-y)) + x/2))
print('ответ :' , round(s , 6) )