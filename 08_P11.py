n=int(input())

data=()
for i in range(n):

    x=set(e for e in input().strip().split())

    data+=(1,tuple(x))

wantAct=input().strip()
data=data[1::2]

check=True
goodAct=dict()
for c in data:

    if wantAct in c:
        check=False

        for m in c:

            if m!=wantAct and m in goodAct:
                goodAct[m]+=1

            elif m!=wantAct and m not in goodAct:
                goodAct[m]=1

if check:
    print('Not Found')
    
elif len(goodAct)==0:
    print('No suggested event')

else:

    most=0
    Act=''
    for c,num in goodAct.items():
        
        if num>most:
            most=num
            Act=c
        elif num==most and c<Act:
            Act=c

    print(Act)
    print(most)
