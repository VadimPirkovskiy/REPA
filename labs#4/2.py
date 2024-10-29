a = int(input())
b = int(input())
c = []
if a < b:
    for i in range(a,b+1):
        c += [i]
if b < a:
    for i in range(a,b-1,-1):
        c += [i]
print(c)