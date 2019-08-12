#lets find all the even fibo nos less than 4000000
mylist=[1,2]
for x in range(0,4000000):
    mylist.append(mylist[-1]+mylist[-2])
    if mylist[-1]>=4000000:
        break
evenfibonos=[]        
for y in mylist:
    if y%2==0:
        evenfibonos.append(y)
print(sum(evenfibonos))        

