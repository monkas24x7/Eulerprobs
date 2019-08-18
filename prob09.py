def pythaprod():
    tot=1000
    for a in range(1,1000):
        for b in range(a+1,1000):
            c=tot-a-b
            if a**2+b**2==c**2:
                prod=a*b*c
    return prod
print(pythaprod())    
