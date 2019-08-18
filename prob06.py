def sqdiff():
    def sqtot():
        tot=0
        for num in range(1,101):
            tot=tot+num**2
        return tot   
    def totsq():
        for num in range(1,101):
            tot2=sum(range(1,101))**2
        return tot2
    return totsq()-sqtot()   
print(sqdiff())

