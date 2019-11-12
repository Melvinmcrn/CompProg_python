s=input().strip().lower()
s1=""
s2=""

for i in range(0,len(s)):

    if s[i] not in " ":
        s1+=s[i]

for i in range(len(s)-1,-1,-1):

    if s[i] not in " ":
        s2+=s[i]
        
if s1==s2:
    print('yes')

else:
    print('no')
