n,m=[int(e) for e in input().strip().split()]
data=set([int(e) for e in input().strip().split()])
num=[int(e) for e in input().strip().split()]

ans=[]
count=0
for k in num:

    check=False
    data_temp1=set(data)

    for c in data:

        data_temp1.discard(c)
        data_temp2=set(data_temp1)

        for i in data_temp1:

            data_temp2.discard(i)
            
            if k-(c+i) in data_temp2:
                check=True
                break

        if check:
            break

    if check:
        ans.append('YES')

    else:
        ans.append('NO')

for c in ans:
    print(c)
