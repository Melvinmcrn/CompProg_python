subjectNum=int(input())

subjectData=dict()
for i in range(subjectNum):

    subject,amount=(e for e in input().strip().split())
    subjectData[subject]=int(amount)

studentNum=int(input())
studentData=dict()
sortedStudent=[]
out=[]

for i in range(studentNum):

    dataTemp=[e for e in input().strip().split()]

    out.append(dataTemp[0])
    studentData[dataTemp[0]]=tuple(dataTemp[2:])

    for i in range(len(sortedStudent)):

        if sortedStudent[i][1]<float(dataTemp[1]):
            sortedStudent.insert(i,(dataTemp[0],float(dataTemp[1])))
            break
        
    else:
        sortedStudent.append((dataTemp[0],float(dataTemp[1])))

out.sort()

for m in sortedStudent:

    for c in studentData[m[0]]:

        if subjectData[c]>0:
            subjectData[c]-=1
            out[out.index(m[0])]=(m[0],c)
            break

for c in out:
    print(c[0],c[1])
