f=input().strip()
n=int(input())

file=open(f)

linecount=0
check_fail=False
line_fail=-1
for line in file:
    
    linecount+=1
    if line.find('Failure',line.rfind(';'))!=-1 and not check_fail:
        line_fail=linecount
        check_fail=True
        
file.close()

file=open(f)

i=1
if check_fail:
    for line in file:
    
        if line_fail-n<=i<=line_fail:
            print(line[line.find(';')+1:-1])
        i+=1

if not check_fail:
    print('Not Found')
