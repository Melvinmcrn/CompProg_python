def eat(q1,q2):

    if (q1[0]-q2[0])**2 == (q1[1]-q2[1])**2:
        return True
    elif q1[0]==q2[0]:
        return True
    elif q1[1]==q2[1]:
        return True

    return False

#-----------------------------------------------------------------------

def all_eat(L):

    out=[]
    for i in range(len(L)-1):
        for j in range(i+1,len(L)):

            if eat(L[i],L[j]):
                out.append((i,j))

    for i in range(len(out)):
        for j in range(len(out)-1):

            if out[j]>out[j+1]:
                out[j], out[j+1] = out[j+1], out[j]

    return out

#main-------------------------------------------------------------------

print(eval(input().strip()))
