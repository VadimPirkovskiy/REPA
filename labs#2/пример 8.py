import math
x = eval(input('введите x : '))
y = float(input('введите y : '))
z = float(input('введите z : '))
s = ((math.exp(abs(x- y)) * abs(x-y)**(x+y))/(math.atan(x) + math.atan(z))) + ((x**6 + math.log(y , math.e)**2)**(1/3))
print( 'Ответ : ' , round(s,4))