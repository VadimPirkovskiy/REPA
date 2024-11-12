def geronugolnik(a,b,c,d,e):
    k1 = (c + d + e ) / 2
    k11 = (k1*(k1 - a ) * (k1 - b )/( k1 - e ))**(1/2)
    k2 = (c + d + e ) / 2
    k22 = (k2*(k2 - c) * (k2 - d) * (k2 - e) )**(1/2)
    s = k11 + k22
    print(s)
geronugolnik(12,3,4,5,6)
