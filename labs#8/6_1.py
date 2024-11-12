def NOD_NOK(a, b):
    i = a
    p = b
    while a != b :
        if a > b :
            a = a - b
        else:
            b = b - a
    print("НОД:" , a)
    m = (i * p)/a
    print("НОК:" , int(m))
NOD_NOK(12,16)
