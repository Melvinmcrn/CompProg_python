row,column = [int(e) for e in input().strip().split()]

data1=[]
for i in range(row):

    data1.append(input().strip().split())

data2=[]
data2+=[0]*row
for i in range(row):

    count=0
    for j in range(column):

        grade=data1[i][j]
        count+=1
        
        if grade=='A':
            data2[i]+=4
        elif grade=='B+':
            data2[i]+=3.5
        elif grade=='B':
            data2[i]+=3
        elif grade=='C+':
            data2[i]+=2.5
        elif grade=='C':
            data2[i]+=2
        elif grade=='D+':
            data2[i]+=1.5
        elif grade=='D':
            data2[i]+=1
        elif grade=='F':
            data2[i]+=0
        elif grade=='X':
            count-=1

    data2[i]/=count

for c in data2:

    print('{:.2f}'.format(c))
