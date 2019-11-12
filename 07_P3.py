file=open('score.txt')

student=[]
for line in file:

    line=line.strip()
    student.append(line.split())

#print(student)

while True:

    x=input().strip()
    if x=='-1':
        break

    for c in student:

        if x in c:
            print(c[1])
            break

    else:

        print('Not Found')
