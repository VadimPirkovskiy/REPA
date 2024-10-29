x = int(input())
y = int(input())
q = 0
w = 0
while y >= q:
    x = x + (x *10)/100
    w += 1
    q += x

print(w)