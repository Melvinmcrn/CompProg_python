n=int(input())

order=[]
for i in range(n):
    
    order.append(int(input()))

out=[1]
outprint='1 '
for i in range(1,n):

    position=out[i-1]-1
    out.append(order[position])
    outprint+=str(out[i])+' '

print(outprint.strip())
