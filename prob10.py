def primesum():   
    z=3
    tot=2   
    def primecheck(n):        
        p = 2       
        while p*p <= n:
            if n % p == 0:                
                return False
            p += 1        
        return True
    while z<=2000000:
        if primecheck(z)==True:
            tot+=z            
        z+=2
    return tot
print(primesum())
