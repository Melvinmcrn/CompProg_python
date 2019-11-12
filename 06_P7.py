s1=input().strip()
s1=s1[1:-1].split(',')

s2=input().strip()
s2=s2[1:-1].split(',')

total=0

for i in range(len(s1)):

    total+=int(s1[i])*int(s2[i])

print(total)
