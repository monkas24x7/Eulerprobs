def sum_eve_fibo():
    a=1
    b=2
    c=0
    tot=0
    while c<4000000:
        c=a+b
        if c%2==0:
            tot+=c        
        a=b
        b=c                
    return tot 
print(sum_eve_fibo())       

