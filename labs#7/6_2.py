w = 3
c = []
p = 0
while w > 0 :
    q = int(input())
    c.append(q)
    w -=1
for i in c :
    if i > 5 :
        p+=i
print(p)
