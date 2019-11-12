s=input().strip()
x1=input().strip()
x2=input().strip()

for i in range(len(s)):

    if s[i] in x1:

        j=x1.find(s[i])
        s=s[:i]+x2[j]+s[i+1:]

    elif s[i] in x2:
        
        j=x2.find(s[i])
        s=s[:i]+x1[j]+s[i+1:]

print(s)
