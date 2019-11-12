def GCD(x,y):

    if x>=y and x%y==0:
        return y
    
    return GCD(y,x%y)

#main===============================================================
x,y = (int(e) for e in input().strip().split())
print(GCD(x,y))
