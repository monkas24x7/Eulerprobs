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
    ans=list(a*b for a in range(100,1000) for b in range(100,1000))
    for item in ans:
        if palindrome(item)==True:
            pali.append(item)
    return max(pali)
print( lpali())




   



