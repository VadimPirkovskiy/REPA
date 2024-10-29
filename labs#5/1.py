n = int(input())
w = []
for i in range(1,n):
    q = i**2
    if q <= n :
        w += [q]
print(w)

