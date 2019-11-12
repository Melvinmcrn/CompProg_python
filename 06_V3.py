file=open(input().strip())
full_list=[]
saved_student=';'

for line in file:

    line=line.strip()

    if len(line)!=0:

        grade=''
        student_id,name,surname,midterm,final=line.split(';')
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

        if ';'+student_id+';' not in saved_student:
            full_list.append(student_list)
            saved_student+=student_id+';'

x='0'

while True:
    
    x=input().strip()
    if x=='-1':
        break
    
    check=True
    for c in full_list:

        if c[0]==x:
            print(c)
            check=False
            break

    if check:
        print('Not Found')

