def x(n):

    if n-1>=0:
        out=x(n-1)
        return 3*out*(1-out)

    if n==0:
        return 0.01

#---------------------------------------------------------------
def M(n):

    if n==0:
        return 1

    if n==1:
        return 1

    out=0
    for k in range(n-1):
        out+=M(k)*M(n-2-k)
        
    return M(n-1)+out

#---------------------------------------------------------------
def D(m,n):

    if m==0 or n==0:
        return 1

    return D(m-1,n) + D(m-1,n-1) + D(m,n-1)

#---------------------------------------------------------------
def S(n):

    if n==1 or n==2:
        return 1

    return int((1/n) * ((6*n - 9) *S(n-1) - (n-3) * S(n-2)))

#---------------------------------------------------------------
def d(n):

    if n==0:
        return 1

    return n*d(n-1) + (-1)**n

#main===========================================================

exec(input().strip())
    
