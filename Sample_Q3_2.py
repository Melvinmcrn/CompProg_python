m,n,p = (int(e) for e in input().strip().split())

matrix1=[]
for i in range(m):
    matrix1.append([int(e) for e in input().strip().split()])

matrix2=[]
for i in range(n):
    matrix2.append([int(e) for e in input().strip().split()])

matrix3=[]
for i in range(m):
    matrix3.append([])
    for j in range(p):
        temp=0
        for k in range(n):
            temp += matrix1[i][k] * matrix2[k][j]

        matrix3[i].insert(j,temp)

for i in range(m):
    out=''
    for j in range(p):
        out+=str(matrix3[i][j])+' '
    print(out.strip())
    
