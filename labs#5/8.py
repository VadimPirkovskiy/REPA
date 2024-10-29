p = 32198435098340968342
c = 0
e = 100000000000000000000000
mix = -10000000000000000000000000000000000000000
while p !=0:
    e = p
    p = int(input())
    if e == p :
        c += 1
        if mix  < c :
            mix  = c
    elif e != p :
        c = 1
print(mix)