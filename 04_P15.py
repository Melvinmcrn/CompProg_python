s=input().strip()
checklaew=""
want=[]

for c in s:

    have=[]
    if c not in checklaew:
#        print('c =',c)
        for i in range(len(s)):

            if s[i]==c:
#                print('have+at',i)
                have.insert(len(have),str(i))
#                print('have=',have)

        checklaew+=c
#        print('len(have)=',len(have))
        if len(have)>1:
            want.insert(len(want),have[1])
        else:
            want.insert(len(want),have[0])
#print('want=',want)
n=len(want)
i=0
out=""

while n>0:

    if str(i) in want:
#        print('i=',i,'s[i]=',s[i])
        out+=s[i]
        n-=1
    i+=1

print(out)
