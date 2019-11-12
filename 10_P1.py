def fac(n):

    out=1
    if n==0:
        out*=1
    if n>=1:
        out=n*fac(n-1)

    return out

#main========================================================
print(fac(int(input())))
