def tiling(n,c):

    if n==1:
        return 1
    out = 0
    for e in 'GRB':
        if c == 'G' and e != 'G':
            out += tiling(n-1,e)
        elif c != 'G':
            out += tiling(n-1,e)
    return out

#main========================================================
N = int(input())
print(tiling(N,'G') + tiling(N,'R') + tiling(N,'B'))
