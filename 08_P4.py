data=tuple([int(e) for e in input().strip().split()])
num=int(input())

count=0
for i in range(len(data)):
    for j in range(i+1,len(data)):

        if data[i]+data[j]==num:
            count+=1

print(count)
