number=list('0123456789')
amount=[0]*10

x=list(input().strip())

for c in x:

    position=number.index(c)
    amount[position]+=1

for c in amount:
    print(c)
