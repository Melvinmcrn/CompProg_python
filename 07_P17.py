data=[]
temp=[]
student_id=''

while True:

    temp=input().strip().split()

    if len(temp)==1:
        student_id=int(temp[0])
        break

    data.append([int(temp[0]),float(temp[1])])

check=False
for i in range(len(data)-1):
    
    if student_id in data[i] or student_id in data[i+1]:
        check=True
        
    for j in range(len(data)-1):

        if data[j][1]<data[j+1][1]:
            data[j],data[j+1]=data[j+1],data[j]

        elif data[j][1]==data[j+1][1]:
            if data[j][0]>data[j+1][0]:
                data[j],data[j+1]=data[j+1],data[j]

#print(data)

if check:

    for c in data:
        if student_id in c:
            print(data.index(c)+1)

else:
    print('Not Found')
