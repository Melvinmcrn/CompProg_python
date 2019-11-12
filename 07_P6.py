n=int(input())

num=[]
sorted_num=[]
total=0
for i in range(n):

    x=int(input())

    total+=x
    sorted_num.append(x)
    for c in num:

        if str(x) in c:

            position=num.index(c)
            num[position][1]+=1
            break

    else:

        num.append([str(x),1])
#    print(num)

#Mean
out=str(total/n)+' '

#Med
sorted_num.sort()

if len(sorted_num)%2==0:
    med=(sorted_num[n//2]+sorted_num[n//2-1])/2

else:
    med=sorted_num[n//2]

out+=str(med)+' '

#Mod
most=[0,0]

for c in num:

    if c[1]>most[1]:
        most=c

out+=str(most[0])
print(out)
