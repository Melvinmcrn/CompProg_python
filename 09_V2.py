def fac(n):
    return str(n)+'!'

#------------------------------------------------------------------------
def oneterm(x,n):
    return str(x)+'**'+str(n)+'/'+str(n)+'!'

#--------------------------------------------------------------------------
def sin(x,n):
    out=str(x)
    k=3
    sign='-'
    for i in range(n-1):
        out+=' '+sign+' '+oneterm(x,k)
        k+=2
        if sign=='-':
            sign='+'
        elif sign=='+':
            sign='-'

    return out  

#-------------------------------------------------------------------------

exec(input().strip())
