row,column= [int(e) for e in input().strip().split()]

matrix1=[]
for i in range(row):

    matrix1.append([int(e) for e in input().strip().split()])

matrix2=[]
for i in range(row):

    matrix2.append([int(e) for e in input().strip().split()])

for i in range(row):
    out=''
    for j in range(column):

        out+=str(matrix1[i][j]+matrix2[i][j])+' '

    print(out)
