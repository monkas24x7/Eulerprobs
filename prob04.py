
def palindrome(num):
    tot=0
    x=num
    
    
    while num!=0:        
        d=num%10
        tot=tot*10+d
        num//=10        
    
    else:
        return tot==x 

pali=[]
def lpali():
    a=99
    b=100
    while a and b :
        a+=1
        b=100         
        while 100<b<999 and 100<a<999:
            if palindrome(a*b)==True:
                pali.append(a*b)
                b+=1 
            else:
                b+=1
           

        #if palindrome(a*b)==True:
        #    pali.append(a*b)
        #    a+=1
        #    b+=1
        #else:
        #    a+=1
        #    b+=1
    return(pali)
print(lpali())


   



