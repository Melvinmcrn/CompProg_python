n=int(input())

s=[]

for i in range(1,n+1):
    s.append(i)

while True:

    a,b= [int(e) for e in input().split()]

    if a==0 and b==0:
        break

    a=s.index(a)
    b=s.index(b)
    
    s[a],s[b]=s[b],s[a]
    
print(s)
