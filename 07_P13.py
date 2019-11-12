row=int(input())
column=int(input())

data=[]
for i in range(row):

    data.append([int(e) for e in input().strip().split()])

out=''
for i in range(row):
    for j in range(i+1,row):

        if data[i]==data[j]:
            out=str(i+1)+'\n'

            for c in data[i]:
                out+=str(c)+' '
            out=out.strip()+'\n'+str(j+1)+'\n'

            for c in data[j]:
                out+=str(c)+' '
            out=out.strip()
            break
        
print(out)
