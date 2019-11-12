s=input().strip().split()
column=len(s)
row=(column+1)//2

table=[s]
for i in range(row-1):
    s=input().strip().split()
    table.append(s)

sum=0
for i in range(-1,-1*(row+1),-1):

    for j in range(-1*(i+1),column+(i+1)):

#        print(table[i][j])
        sum+=int(table[i][j])

print(sum)
