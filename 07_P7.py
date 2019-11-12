file=open('score.txt')

student=[]
for line in file:

    line=line.strip()
    ID,score=line.split()
    student.append(ID)

student.sort()

for c in student:
    print(c)
