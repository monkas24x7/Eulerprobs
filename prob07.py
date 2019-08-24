def Optimus_prime():    
    c=1
    def primecheck(n):        
        p = 2       
        while p*p <= n:
            if n % p == 0:                
                return False
            p += 1        
        return True
    z=3
    while c<=10000:
        if primecheck(z):
            c+=1
            promo=z
        z+=2
    return promo
print(Optimus_prime())

