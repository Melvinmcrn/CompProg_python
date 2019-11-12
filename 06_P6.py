s=input().strip().split()
out=''

for i in range(len(s)):

    if len(s)==1:
        out=s[i]
    elif i==0:
        out+=str(int((float(s[i])+float(s[i+1]))//2))
    elif i==len(s)-1:
        out+=str(int((float(s[i])+float(s[i-1]))//2))
    else:
        out+=str(int((float(s[i-1])+float(s[i])+float(s[i+1]))//3))
    out+=' '

print(out.strip())
