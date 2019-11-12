num=[]
most=['i',0]
count=0
while True:

    x=input().strip()
    if x=='-1':
        break

    count+=1
    for c in num:

        if x in c:
            position=num.index(c)
            num[position][1]+=1
            if num[position][1]>most[1]:
                most=num[position]
            break

    else:
        num.append([x,1])


if most[1]>count/2:

    print(most[0])

else:

    print('Not found')
