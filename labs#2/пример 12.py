import math
x = float(input('введите x : '))
y = float(input('введите y : '))
z = eval(input('введите z : '))
s = 2**(y**x)+((3**x)**y)-(y*(math.atan(z)-(1/3)))/(abs(x)+(1/(y**2+1)))
print('ОТВЕТ : ',round(s,5))

