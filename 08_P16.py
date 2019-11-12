n=int(input())

data=[]
Union=set()
Intersect=set()

for i in range(n):

    x=set(input().strip().split())

    if i==0:
        Union=x
        Intersect=x
    else:
        Union=Union.union(x)
        Intersect=Intersect.intersection(x)

print(len(Union))
print(len(Intersect))

