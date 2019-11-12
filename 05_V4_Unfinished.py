s=input().strip()
x1=input().strip()
x2=input().strip()
x3=input().strip()

file=open(s,"r")

charactor=""
number=[]

for line in file:
    for c in line:

        if c in charactor:
            n=charactor.find(c)
            number.insert(n,number[n]+1)

        else:
            charactor+=c
            number.insert(len(number),1)

file.close()

nx1=number[charactor.find(x1)]
positionx1=charactor.find(x1)
nx2=number[charactor.find(x2)]
positionx2=charactor.find(x2)
nx3=number[charactor.find(x3)]
positionx3=charactor.find(x3)

most=max(nx1,nx2,nx3)
out=charactor[number.find(most)]

if nx1==most:
    most=max(nx2,nx3)
    least=min(nx2,nx3)
elif nx2==most:
    most=max(nx1,nx3)
    least=min(nx1,nx3)
elif nx3==most:
    most=max(nx2,nx1)
    least=min(nx2,nx1)
out+=charactor[number.find(most)]+charactor[number.find(least)]
print(out)

