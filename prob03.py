def maxprime(num):
    x = 2
    p_factors = []
    while x*x<= num:
        if num %x:
            x=x+ 1
        else:
            num=num/x
            p_factors.append(x)
    if num > 1:
        p_factors.append(num)
    return max(p_factors)
print(maxprime(600851475143))  

    



    
