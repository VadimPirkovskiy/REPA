def chocol(n,m,k):
    c=0
    if (k%n==0 and k/n<=m):
        c+=1
        if n == 1 and k<=m:
            c+=1
    elif (k%m==0 and k/m<=n):
        c+=1
        if m == 1 and k<=n:
            c+=1
    if c >= 1 :
        print('Да')
    else:
        print('Нет')
#несовсем понял можно ли не ломать шоколадку вовсе , но предусмотрел и такое