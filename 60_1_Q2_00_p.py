def list2dict(x):

    d=dict()
    for c in x:
        if c[1][1] not in d:
            d[c[1][1]] = [(c[0],c[1][0])]
        else:
            d[c[1][1]].append((c[0],c[1][0]))

    return d

#----------------------------------------------------------------
def dict2list(d):

    x = list()
    for i,v in d.items():
        for c in v:
            x.append([c[0],(c[1],i)])

    return x

#----------------------------------------------------------------
def get_empty(d):

    ans = set()
    for i,v in d.items():
        if len(v)==0:
            ans.add(i)

    return ans

#----------------------------------------------------------------
def compress_string(s):

    out=[]
    temp=None
    for c in s:
        if temp==None:
            count = 1
            temp = c
        elif c==temp:
            count += 1
        elif c!=temp and temp!=None:
            out.append((temp,count))
            temp = c
            count = 1
    else:
        if len(s)>0:
            out.append((temp,count))

    return tuple(out)

#----------------------------------------------------------------
def a(n):

    if n==0:
        return 3
    if n==1:
        return 1
    if n%2!=0 and n>1:
        return 3*a(n-1) - 2*a(n-2) - n
    if n%2==0 and n>0:
        return 2*a(n-1) + a(n-2) + 3

#main===========================================================

exec(input().strip())
exec(input().strip())
