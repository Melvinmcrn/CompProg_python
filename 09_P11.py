def sd(L,mean):

    x=0
    for c in L:
        x+=(c-mean)**2

    return (x/len(L))**0.5

#---------------------------------------------------------

def meanscore(L):

    return sum(L)/len(L)

#---------------------------------------------------------

def zscore(L):

    mean=meanscore(L)
    SD=sd(L,mean)

    out=[]
    for c in L:
        out.append((c-mean)/SD)

    return out

#main-----------------------------------------------------

L = [float(e) for e in input().split()]
for i in zscore(L):
    print(i)
