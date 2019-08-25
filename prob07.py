def prime():    
    c=1
    z=3
    def primecheck(n):        
        p = 3
        if n%2==0:
            return False       
        while p*p <= n:
            if n % p == 0:                
                return False
            p+=2       
        return True
    while c<=10000:
        if primecheck(z):
            c+=1
            promo=z
        z+=2
    return promo
print(prime())


