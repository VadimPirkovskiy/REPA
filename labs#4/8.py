n = int(input())
k = []
while n > 0 :
    for i in range(1,n+1):
        k+= [i]
        p = list(k)
        print(*p, sep='')
        n -=1