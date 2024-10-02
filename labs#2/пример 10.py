import math
x = eval(input('введите x : '))
y = eval(input('введите y : '))
z = float(input('введите z : '))
s = (2**-x)*(math.sqrt(x + ((abs(y)**(1/4)))))*(math.exp(x-(1/math.sin(z))))**(1/3)
print( ' ОТВЕТ : ',round(s,5))