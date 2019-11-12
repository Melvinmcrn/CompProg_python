row,column=[int(e) for e in input().strip().split()]

data=[]
for i in range(row):

    data.append([int(e) for e in input().strip().split()])

column_data=[]
for j in range(column):
    temp=[]
    for i in range(row):
        temp.append(data[i][j])

    column_data.append(temp)

check=True
for i in range(row):
    for j in range(column):

        if data[i][j]==min(data[i]) and data[i][j]==max(column_data[j]):
            print(data[i][j])
            check=False
            break
    if not check:
        break

if check:
    print(-1)
