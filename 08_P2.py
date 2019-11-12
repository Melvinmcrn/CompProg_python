n=int(input())

data=dict()
name=()
for i in range(n):

    temp_input=input().strip().split(', ')
    name+=tuple([temp_input[0]])

    for c in temp_input[1:]:

        if c not in data:
            data[c]=tuple([temp_input[0]])

        else:
            data[c]=data[c]+(tuple([temp_input[0]]))

order=input().strip().split(', ')

out=[]
for c in order:

    if c not in data:
        out.append(c+' -> Not found')

    else:

        temp=''
        for m in data[c]:
            temp+=m+', '
        out.append(c+' -> '+temp[:-2])

for c in out:
    print(c)
