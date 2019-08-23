def primefind(n):     
    c=0      
    x = [True for y in range(0,n+1)]    
    for p in range(4,n+1,2):
        x[p]= False
    for p in range(3, n+1, 2):
        if c<=9999:
            if x[p] == True:
                z=p
                c+=1            
                for y in range(p * p, n+1, 2*p): 
                    x[y] = False
        else:
            break          
    return z
print(primefind(3000000))
