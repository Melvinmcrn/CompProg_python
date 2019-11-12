n=int(input())
data=set()

for i in range(n):

    x=tuple(e for e in input().strip().split())

    data.add(x)

order=tuple(input().strip().split())
data_temp=set(data)

for c in data_temp:

    for m in order:

        if m not in c or (m not in c[1:] and m in c[0]):
            data.discard(c)
            break
out=[]

check=True
for c in data:

    if check:
        out.append(c)
        check=False

    else:

        for m in out:
            
            if c[0]<m[0]:
                out.insert(out.index(m),c)
                break

        else:
            out.append(c)

for c in out:
    print(c[0],c[1],c[2],c[3])

if len(out)==0:
    print('Not Found')
