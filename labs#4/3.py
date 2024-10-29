a = int(input())
b = int(input())
c = []
for i in range(b,a-1,-1):
    if i%2 != 0:
        c += [i]
print(c)


