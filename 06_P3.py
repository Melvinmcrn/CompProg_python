n=int(input())

s=[]
total=0

s=input().strip().split()

for i in range(n):
    total+=int(s[i])
    
print(total/n)
