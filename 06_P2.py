size=int(input())

s=[]

for i in range(size):

    x=int(input())
    s.append(x)

start,stop=[int(e) for e in input().split()]

sum=0

for i in range(start,stop+1):
    sum+=s[i]

print(sum)
