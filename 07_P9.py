num=[int(e) for e in input().split()]
even=[] # %2==0
odd=[]  # %2!=0

for c in num:

    if c%2==0:
        even.append(c)

    else:
        odd.append(c)

even.sort()
odd.sort(reverse=True)

out=''
for c in even:
    out+=str(c)+' '

for c in odd:
    out+=str(c)+' '

print(out.strip())
