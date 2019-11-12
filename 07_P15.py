n=int(input())

data=[]
for i in range(n):

    data.append([int(e) for e in input().strip().split()])

for k in range(n):

    check1=True
    for j in range(n):
        
        i=k
        if i!=j and data[i][j]==1:
            check1=False
            break

    if check1:

        check2=True
        for i in range(n):

            j=k
            if data[i][j]==0:
                check2=False
                break

    if check1 and check2:
        print(k)
        break

if not check1 or not check2:
    print(-1)
