n = int(input('сколько минут прошло с начала дня ? : '))
x = n//60
if x > 23 :
    x = x % 24
z = n%60
if x > 4 and x < 20 :
    w = 'Часов'
else:
    w = 'Часа'



print('Прошло',x,w,z,'минут')