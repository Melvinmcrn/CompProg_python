n = int(input())

data = dict()
data_list = []
for i in range(n):
    temp = [e for e in input().strip().split()]
    data_list.append(temp[0])
    temp_list = []
    for c in temp[1:]:
        temp_list.append(float(c))
    data[temp[0]] = temp_list

order = input().strip().split()

if order[0] == 'show':

    for c in data_list:
        out = c
        for m in data[c]:
            out += ' ' + str(m)

        print(out)

elif order[0] == 'get':

    if order[1] not in data:
        print(order[1],'not found')
    else:
        out = order[1]
        for c in data[order[1]]:
            out += ' ' + str(c)

        print(out)
        
elif order[0] == 'avg':

    out=0
    for c in data.values():
        out += c[int(order[1])-1]
    print(round(out/n,4))

elif order[0] == 'max':

    m = int(order[1])-1
    out = ['',0]
    for i,v in data.items():
        if v[m] > out[1]:
            out = [i,v[m]]
        elif v[m] == out[1] and i < out[0]:
            out = [i,v[m]]
    print(out[0],out[1])

elif order[0] == 'sort':

    out=[]
    for i,v in data.items():
        v = v[int(order[1])-1]

        if len(out) == 0:
            out.append([i,v])
        else:
            for j in range(len(out)):
                if out[j][1] > v:
                    out.insert(j,[i,v])
                    break
                elif out[j][1] == v and out[j][0] > i:
                    out.insert(j,[i,v])
                    break
            else:
                out.append([i,v])

    out_print = ''
    for c in out:
        out_print += c[0] + ' '

    print(out_print.strip())
