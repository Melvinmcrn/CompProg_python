def KS(i,w,v,x):  
    if i<0:
        return 0
    if x>=w[i]:
        out = max(KS(i-1,w,v,x),KS(i-1,w,v,x-w[i])+v[i])
        return out
    if x<w[i]:
        out = KS(i-1,w,v,x)
        return out

#main==========================================================

w = [int(e) for e in input().strip().split()]
v = [int(e) for e in input().strip().split()]
x = int(input())
print(KS(len(w)-1,w,v,x))
