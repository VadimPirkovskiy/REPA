def slolco(q,w,e):
    if q==w==e :
        print(3)
    else:
        if q==w or w==e or e==q:
            print(2)
        else:
            print(0)