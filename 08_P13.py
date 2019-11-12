data=dict()

while True:
    
    x=[e for e in input().strip().split()]

    if len(x)==1:
        thisLocation=x[0]
        break

    if x[0] in data and x[1] not in data[x[0]]:
        data[x[0]]=data[x[0]]+[x[1]]

    else:
        data[x[0]]=[x[1]]

    if x[1] in data and x[0] not in data[x[1]]:
        data[x[1]]=data[x[1]]+[x[0]]
        
    else:
        data[x[1]]=[x[0]]

out={thisLocation}
if thisLocation in data:
    for c in data[thisLocation]:
        out.add(c)
        for m in data[c]:

            out.add(m)

out=list(out)
out.sort()

for c in out:
    print(c)
    
