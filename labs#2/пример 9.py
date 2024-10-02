import math
x = eval(input('введите x : '))
y = float(input('введите y : '))
z = eval(input('введите z : '))
s =abs(x**(y/x) - (y/x)**(1/3)) +(y-x)*((math.cos(y)-(z/(y-x)))/(1+(y-x)**2))
print('ответ : ' , round(s,5))