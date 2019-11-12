def mod(a,k,m):

    if k==0:
        return 1
    else:
        temp = (mod(a,k//2,m))**2
        if k%2==0:
            return temp%m

        elif k%2!=0:
            return a*temp % m


    
#main=========================================================
a,k,m = (int(e) for e in input().split())

print(mod(a,k,m))
