import random

def qsort(d):

    if len(d)<=1:
        return d
    p = d[random.randint(0,len(d)-1)]
    le = [e for e in d if e<p]
    eq = [e for e in d if e==p]
    mo = [e for e in d if e>p]
    le = qsort(le)
    mo = qsort(mo)
    return le+eq+mo
    
#main==========================================================

d = [int(e) for e in input().split()]
d = qsort(d)
print(' '.join([str(e) for e in d]))
    
