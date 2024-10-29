n = int(input())
minq=1000000000000000000000000000000000000000000
if n >=2 :
    for i in range(2,n+1):
        if n%i==0:
            if minq>i :
                minq = i
print(minq)