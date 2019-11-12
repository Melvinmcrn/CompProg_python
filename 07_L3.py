d=[int(e) for e in input().split()]
n=len(d)

for k in range(n-1):
    for l in range(n-1):

        if d[l] > d[l+1]:
            d[l],d[l+1]=d[l+1],d[l]

if n%2==0:

    print((float(d[n//2])+float(d[n//2-1]))/2)

else:

    print(float(d[n//2]))
