def f(d,c,s,b,m):

    if s == len(d)-1:
        return m+1

    if b and d[s+1] >= d[s]:
        return f(d,c+1,s+1,True,max(c+1,m))

    if b and d[s+1] < d[s]:
        return f(d,0,s+1,False,m)

    if not b and d[s+1] >= d[s]:
        return f(d,1,s+1,True,m)

    return f(d,0,s+1,False,m)

#main============================================================

d = [int(e) for e in input().split()]
print(f(d,0,0,False,0))
