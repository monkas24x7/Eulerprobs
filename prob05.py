import math
def lcm():
    def find_lcm(num1, num2):
        num=int(num1*num2)
        den=int(math.gcd(num1,num2))
        lcm=int(num/den)
        return lcm
         
    l = range(1,21)

    num1 = l[0] 
    num2 = l[1] 
    lcm = find_lcm(num1, num2) 
    
    for i in range(2, len(l)): 
        lcm = find_lcm(lcm, l[i]) 
        
    return lcm
print (lcm())



    
