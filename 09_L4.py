def row_number(t, e) :

#    print(t,e)
    for i in range(len(t)):
#        print('e=',e,'t=',t,'i=',i,'t[i]=',t[i])
        if e in t[i]:
            return i
    else:
        return

#-------------------------------------------------------------

def flatten(t) :

    out=[]
    for d in t:
        for c in d:
            if c!=0:
                out.append(c)

    return out
            
#-------------------------------------------------------------

def inversions(x):

    count=0
    for i in range(len(x)):
        for j in range(i+1,len(x)):

            if x[i]>x[j]:
                count+=1

    return count

#-------------------------------------------------------------

def solvable(t):

    flat=flatten(t)
    inver=inversions(flat)
#    print(flatten(t))
#    print(inver)
    
    if len(t)%2!=0:
        if inver%2==0:
            return True
        else:
            return False

    elif len(t)%2==0:
        if (inver%2!=0 and row_number(t,0)%2==0) or (inver%2==0 and row_number(t,0)%2!=0):
            return True
        else:
            return False

#-------------------------------------------------------------

exec(input().strip())
