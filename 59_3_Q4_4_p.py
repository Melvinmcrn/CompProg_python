data = dict()
while True:

    x = input().strip().split()
    if x == ['done']:
        break
    
    data[x[0]] = x[1:]

order = input().strip().split()

if order[0] == 'R':

    out = []
    for i,v in data.items():
        out.append((i,len(v)))

    out.sort()
    for c in out:
        print(c[0],c[1])

elif order[0] == 'T':

    like = dict()
    for i,v in data.items():
        for c in v:
            if c in like:
                like[c] += 1
            else:
                like[c] = 1

    most_like = [(0,0)]
    for i,v in like.items():
        if v > most_like[0][1]:
            most_like = [(i,v)]
        elif v == most_like[0][1]:
            most_like.append((i,v))

    most_like.sort()
    for c in most_like:
        print(c[0])

elif order[0] == 'C':

    out = []
    for i,v in data.items():
        if order[1] in v and order[2] in v:
            out.append(i)

    if len(out) == 0:
        print('None')
    else:
        out.sort()
        for c in out:
            print(c)

elif order[0] == 'M':

    out = set()

    for i,v in data.items():
        for c in v:
            if c in data:
                if i in data[c]:
                    out.add((i,c))
                    out.add((c,i))

    if len(out) == 0:
        print('None')
    else:
        out = sorted(list(out))
        for c in out:
            print(c)
