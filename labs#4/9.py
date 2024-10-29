n = int(input())
x = n
i = 0
e = 0
w = 1
z = [0]
while x > 1:
    e = i + w
    w = i
    i = e
    z +=[e]
    x -= 1
print(sum(z))

