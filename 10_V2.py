def h(n):

    if n>=1:
        return 2*h(n-1)+1

    if n==0:
        return 0

#------------------------------------------------------------

def gcd(x,y):

    if y>0:
        return gcd(y,x%y)

    if y==0:
        return x

#------------------------------------------------------------

def J(n,k):

    if n>1:
        return (J(n-1,k)+k)%n

    if n==1:
        return 0

#------------------------------------------------------------

def C(n):

    if n-1>=0:
        out=0
        for k in range(n):
            out+=C(k)*C(n-1-k)

        return out
    if n==0:
        return 1

#------------------------------------------------------------

def f(n):

    if n>=2 and n%2!=0:
       return (f(int((n+1)/2)))**2 + (f(int((n-1)/2)))**2

    if n>=2 and n%2==0:
      return  (2*f(int(n/2)-1) + f(int(n/2))) * f(int(n/2))

    if n==0:
        return 0

    if n==1:
        return 1

#------------------------------------------------------------

def F(n):

    if n>0:
        return n-M(F(n-1))
        
    if n==0:
        return 1

#------------------------------------------------------------

def M(n):

    if n>0:
        return n-F(M(n-1))

    if n==0:
        return 0

#------------------------------------------------------------

def A(m,n):

    if m>0 and n==0:
        return A(m-1,1)

    if m>0 and n>0:
        return A(m-1,A(m,n-1))

    if m==0:
        return n+1

#main========================================================

exec(input().strip())
