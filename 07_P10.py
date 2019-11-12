n=int(input())

data=[]
for i in range(n):
    
    data.append(input().strip())

count=0
for i in range(n-1):
    for j in range(n-1):
        
        if len(data[j])>len(data[j+1]):
            data[j],data[j+1]=data[j+1],data[j]
            count+=1

        elif len(data[j])==len(data[j+1]):
            
                if data[j]>data[j+1]:
                    data[j],data[j+1]=data[j+1],data[j]
                    count+=1
                    
for c in data:

    print(c)

print(count)
