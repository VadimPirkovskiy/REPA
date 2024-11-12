a = [10,2,3,4,5,6,7,8,9,1]
mx = -1000000000000
for i in a :
    if i > mx :
        mx = i

p = len(a)
w = sum(a)
w = w/p
q = []
for i in a :
    if w < i and i < mx :
        q.append(i)
print(q)