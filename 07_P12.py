order,n = [int(e) for e in input().strip().split()]

matrix=[]
for i in range(n):

    matrix.append([int(e) for e in input().strip().split()])

total=0
if order==0:

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):

            if i>=j:
                total+=matrix[i][j]
    
elif order==1:

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):

            if i<=j:
                total+=matrix[i][j]
                
print(total)
