#What is the largest prime factor of the number 600851475143 ?

primenos=[]
primefacs=[]
def maxpf(num):
    x=3
    while x<=num:
        for y in range(3,x,2):
            if x%y==0:
                x+=2
                break
        else:
            if num%x==0:
                primefacs.append(x)
                x+=2
            else:
                x+=2
                continue
    #for item in primenos:
     #   if num%item==0:
      #      primefacs.append(item)

    return max(primefacs)
print(maxpf(600851475143))


    



    
