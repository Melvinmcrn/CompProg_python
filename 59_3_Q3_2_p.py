d0 = [int(e) for e in input().strip().split()]
d1 = [int(e) for e in input().strip().split()]
c  = input().strip()

out = []

if c == 'z':
    m = min(len(d0), len(d1))
    for i in range(m):
        out.append(d0[i])
        out.append(d1[i])

    if len(d0) > len(d1):
        for i in range(m,len(d0)):
            out.append(d0[i])
    else:
        for i in range(m,len(d1)):
            out.append(d1[i])

else:
    i=0
    j=0

    while i<len(d0) and j<len(d1):
        if d0[i] < d1[j]:
            out.append(d0[i])
            i+=1
        else:
            out.append(d1[j])
            j+=1
    for k in range(i,len(d0)):
        out.append(d0[k])
    for k in range(j,len(d1)):
        out.append(d1[k])

print(out)
