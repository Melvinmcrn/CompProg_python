def nextEven(f): #Jum nuan koo

    if (f//1+1)%2==0:
        return int(f//1+1)
    else:
        return int(f//1+2)

#-------------------------------------------------------------------

def nextOdd(f): #Jum nuan kee

    if (f//1+1)%2!=0:
        return int(f//1+1)
    else:
        return int(f//1+2)

#main---------------------------------------------------------------

while True:
    x=float(input())
    if x<0:
        break

    even = nextEven(x)
    odd  = nextOdd(x)
    print( (even, odd) )
