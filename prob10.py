def primesum(n):    
    t=2        
    x = [True for y in range(0,n+1)]    
    for p in range(4,n+1,2):
        x[p]= False
    for p in range(3, n+1, 2):
        if x[p] == True:
            t+=p            
            for y in range(p * p, n+1, 2*p): 
                x[y] = False         
    return t
print(primesum(2000000))
