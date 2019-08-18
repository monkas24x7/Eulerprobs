def maxprimefac(n):
    p=2 
    
    primenos=[] 
    primefacs=[]
    x = [True for y in range(0,n)]    
    while (p * p <= n):              
        if x[p] == True:            
            for y in range(p * p, n, p): 
                x[y] = False        
        p += 1       
    for p in range(2, n): 
        if x[p]==True:
            primemos.append(p) 
    for item in primenos:
        if n%item==0:
            primefacs.append(p)          
            
        
    return max(primefacs)
print(maxprimefac(600851475143))

    



    
