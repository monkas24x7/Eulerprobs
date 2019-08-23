def sqdiff():
    n=100
    def sqtot():
        tot= n*(n+1)*(2*n+1)/6
        return tot   
    def totsq():
        tot2=(sum(range(1,101)))**2
        return tot2
    return totsq()-sqtot()   
print(sqdiff())


