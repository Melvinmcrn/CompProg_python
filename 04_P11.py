s=input().strip()
x1,x2=[int(num) for num in input().split()]

out=""

for i in range(len(s)):

    if x1<=i<=x2:
        out+=s[x1+x2-i]

    else:
        out+=s[i]

print(out)
