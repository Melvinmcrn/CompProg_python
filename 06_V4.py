file=open(input().strip())

out=[]
count=[]
for line in file:

    line=line.strip()

    if len(line)!=0:

        fruit,name=line.split()

        check=True
        for i in range(len(out)):

            if fruit in out[i]:
                check=False
                out[i][1].append(name)
                count[i]=count[i]+1

        if check:
            out.append([fruit,[name]])
            count.append(1)

#for i in range(len(out))
print(out)
max_position=count.index(max(count))
print('The most favorite fruit is',out[max_position][0])
