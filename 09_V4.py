def make_int_list(x):
    x=x.split()
    out=[]
    for c in x:
        out.append(int(c))
    return out

#----------------------------------------------------------

def is_odd(e):
    return e%2!=0

#---------------------------------------------------------

def odd_list(alist):
    out=[]

    for c in alist:
        if c%2!=0:
            out.append(c)

    return out

#--------------------------------------------------------

def sum_square(alist):

    out=0
    for c in alist:
        out+=c**2

    return out

#--------------------------------------------------------

exec(input().strip())
