s=input().strip()
n=0
num=""
if s[0] not in "+-":
    s='+'+s

for i in range(len(s)):
    
    if s[i] in '+':
        j=i+1
        while j<len(s):
            if s[j] in '+-':
                break
            num+=s[j]
            j+=1
            
        n+=int(num)
        num=""

    elif s[i] in '-':
        j=i+1
        while j<len(s):
            if s[j] in '+-':
                break
            num+=s[j]
            j+=1
        
        n-=int(num)
        num=""
    
print(n)
