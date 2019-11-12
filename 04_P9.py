s=input().strip()
x1=input().strip()
x2=input().strip()

for i in range(len(s)):

    if s[i]==x1:

        s=s[:i]+x2+s[i+1:]

    elif s[i]==x2:

        s=s[:i]+x1+s[i+1:]

print(s)
