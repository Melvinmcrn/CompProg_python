x=input().strip().lower()

check=0
for i in range(1,len(x)):

    if x[i-1]>x[i]:
        check+=1

if check>0:
    print("no")

else:
    print("yes")
