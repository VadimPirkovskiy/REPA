n = str(input())
k = len(n)
c = 0
for i in range(0, k):
    if n[i]==':' :
        c += 1
n = n.replace(':' , '%')

print(c ,n)