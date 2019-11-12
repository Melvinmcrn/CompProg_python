file=open(input().strip())

courses=dict()
for line in file:

    temp=tuple(line.strip().split(','))

    courses[temp[0]]=temp[1]

file.close()

file=open(input().strip())

teachers=dict()
for line in file:

    temp=tuple(line.strip().split(','))

    teachers[temp[0]]=temp[1]

file.close()

file=open(input().strip())

database=[]
for line in file:

    temp=tuple(line.strip().split(','))

    database.append(temp)

file.close()

for c in database:

    if c[0] not in courses or c[1] not in teachers:
        print('record error')

    else:

        print(courses[c[0]]+','+teachers[c[1]])
        
