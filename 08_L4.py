file=open('books.txt')

name=[]
data=dict()
for line in file:

    line=line.strip()

    temp=line.split(', ')
        
    data[temp[0]]=tuple(temp[1:])
    name.append(temp[0])

file.close()
    
x=input().strip().split(', ')

out=[]
check=True
for c in data:

    for m in x:

        #print('m=',m,'data[c]=',data[c])
        if m not in data[c]:
            break

    else:
        out.append(c)
        #print(out)
        check=False

if check:
    print('Not found')
            
else:

    for c in name:
        if c in out:
            print(c)
