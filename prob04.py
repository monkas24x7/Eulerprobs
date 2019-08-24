def lpali():
    z=0
    for a in range(100,1000):
        for b in range(100,1000):
            a*b
            if str(a*b)==str(a*b)[::-1] and a*b>z:
                z=a*b
    return z

print( lpali())




   



