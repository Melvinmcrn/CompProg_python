data=list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'+'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower())
#print(data)
amount=[0]*62

x=list(input().strip())

for c in x:

    position=data.index(c)
    amount[position]+=1

out=''

for c in amount:

    out+=str(c)+' '

print(out.strip())
