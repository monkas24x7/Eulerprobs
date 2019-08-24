import math
def lcm():
    def find_lcm(num1, num2):
        num=int(num1*num2)
        den=int(math.gcd(num1,num2))
        lcm=int(num/den)
        return lcm
    c=1
    num1 = 1
    num2 = 2
    while c<21:         
        lcm = find_lcm(num1, num2)
        num1=lcm
        num2+=1
        c+=1         
    return lcm
print (lcm())




    
