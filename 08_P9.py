data=dict()

n=int(input())

for i in range(n):

    x=int(input())

    if x in data:
        data[x]+=1

    else:
        data[x]=1

most=0
num=0
for c in data.items():

    if c[1]>most:
        most=c[1]
        num=c[0]

    elif c[1]==most and c[0]<num:
        num=c[0]

print(num)

