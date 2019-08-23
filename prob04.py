def palindrome(num):
    tot=0
    x=num   
    while num!=0:        
        d=num%10
        tot=tot*10+d
        num//=10         
    
    return tot==x 

pali=[]
def lpali():
    z=0
    for a in range(100,1000):
        for b in range(100,1000):
            a*b
            if palindrome(a*b)==True and a*b>z:
                z=a*b
    return z

print( lpali())




   



