n = str(input())
k = len(n)
c = 0
for i in range(0,k):
    if n[i]=='а':
        c+=1
    if n[i]=='a':
        c+=1
u = n.split('а')
u = str(u)
u = u.split('a')
u = ''.join(u)a
e = str(u)
print(c,e)
