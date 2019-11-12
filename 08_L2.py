file=open('address.txt')

addr=dict()

for line in file:

    line=line.strip().split()

    addr[(line[0],line[1])]=(line[2])

while True:

    x=input().strip()
    if x=='':
        break

    x=tuple(x.split())

    if x in addr:
        print(addr[x])

    else:

        for c in addr:

            if addr[c] in x:
                print(c[0],c[1])
                break

        else:
            print('Not Found')
