file=open(input().strip())
full_list=[]

for line in file:

    grade=''
    student_id,name,surname,midterm,final=line.strip().split(';')
    score=float(midterm)+float(final)
    
    if 80<=score<=100:
        grade='A'
    elif 70<=score<80:
        grade='B'
    elif 60<=score<70:
        grade='C'
    elif 50<=score<60:
        grade='D'
    else:
        grade='F'

    student_list=[student_id,name+' '+surname,grade]

    full_list.append(student_list)

print(full_list)
