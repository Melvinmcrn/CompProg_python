def copylist(x):

    out=[]
    for c in x:
        if type(c) is list:
            out.append(copylist(c))

        else:
            out.append(c)

    return out

#main=================================================

exec(input().strip())
