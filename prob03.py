def maxprime(num):
    x = 2
    p_factors = []
    while x*x<= num:
        if num %x:
            x=x+ 1
        else:
            num=num/x
            y=x
    if num > 1:
        y=num
    return y
print(maxprime(600851475143))  

    



    
