data=dict()
while True:
    
    x=input().strip()
    if x=='-1':
        break

    temp=x.split()
    for c in temp[1:]:
        
        if c not in data:
            data[c]={temp[0]}
            
        else:
            data[c]=data[c].union({temp[0]})

course1,course2=[e for e in input().strip().split()]
student1=set()
student2=set()

if course1 in data:
    student1=data[course1]
if course2 in data:
    student2=data[course2]

out1=str(len(student1.intersection(student2)))
out2=str(len(student1^student2))
out3=str(len(student1.union(student2)))

print(out1+' '+out2+' '+out3)
