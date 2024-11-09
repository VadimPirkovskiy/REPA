f = str(input())
f = f.split(' ')
c = f
p = 0
for i in c :
    if i[0]=='е' or i[0]=='Е':
        p += 1
print(p)

