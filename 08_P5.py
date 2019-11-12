data=set([int(e) for e in input().strip().split()])
num=int(input())
data_temp=set(data)

count=0
for c in data:

    data_temp.discard(c)
    if num-c in data_temp:
        count+=1

print(count)
