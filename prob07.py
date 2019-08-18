def primefind(n):
    p=2 
    primes=[]      
    x = [True for y in range(0,n)]    
    while (p * p <= n):              
        if x[p] == True:            
            for y in range(p * p, n, p): 
                x[y] = False        
        p += 1       
    for p in range(2, n): 
        if x[p]==True: 
            primes.append(p)
    return primes[10000]
print(primefind(2000000))
