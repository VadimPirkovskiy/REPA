a = int(input())
b = int(input())
c = []
if a < b :
    for i in range(a , b+1):
        c +=[i]
else:
    print('неудовлетворяет условия')
print(c)