n = int(input())
x = 1
i = 2
maxx = - 100000000000
maxxx = -1000000000000
while i <= n :
    i = i *2
    x += 1
    if maxx < i and i < n :
        maxx = i
        maxxx = x
print(maxx , maxxx)