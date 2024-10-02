import math
x = eval(input('введите x : '))
y = eval(input('введите y : '))
z = float(input('введите z : '))
s = ((math.log(y**-((abs(x**(1/2)))),math.e))*(x-(y/2)))+(math.sin(math.atan(z))**2)
print('ОТВЕТО :' , round(s , 3))
