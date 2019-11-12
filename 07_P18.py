charactor='abcdefghijklmnopqrstuvwxyz'

n=int(input())

data=[]
num=[]

#make a number list
for i in range(n):
    num+=[[0]*26]

#input a number list
for i in range(n):

    data.append(input().strip())

    temp=[]

    for c in data[i]:

        position=charactor.index(c)
        num[i][position]+=1

#swap the list
for i in range(n-1):
    for j in range(n-1):

        for k in range(26):

            if num[j][k]<num[j+1][k]:
                break
            elif num[j][k]>num[j+1][k]:
                data[j],data[j+1]=data[j+1],data[j]
                num[j],num[j+1]=num[j+1],num[j]
                check=False
                break
        else:
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
                num[j],num[j+1]=num[j+1],num[j]

for c in data:
    print(c)
