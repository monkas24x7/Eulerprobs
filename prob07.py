def primefind(n):     
    primes=[]      
    x = [True for y in range(0,n+1)]    
    for p in range(4,n+1,2):
        x[p]= False
    for p in range(3, n+1, 2):
        if x[p] == True:            
            for y in range(p * p, n+1, 2*p): 
                x[y] = False        
          
    for p in range(2, n): 
        if x[p]==True: 
            primes.append(p)
    return primes[10000]
print(primefind(3000000))
