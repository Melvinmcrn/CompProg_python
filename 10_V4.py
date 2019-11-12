def sumlist(x):

    out=0

    for c in x:
        if type(c)==list:
            out+=sumlist(c)
        if type(c)==int:
            out+=c

    return out

#main======================================================

print(sumlist(eval(input().strip())))
