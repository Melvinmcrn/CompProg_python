data=input().strip().split(', ')

count=0
for i in range(1,len(data)-1):

    if int(data[i])<0 and int(data[i-1])>=0:
        count+=1

print(count)
