s=input().strip()
x=0
y=0

for c in s:

    if c=='U':
        y+=1
        
    elif c=='D':
        if y!=0:
            y-=1

    elif c=='L':
        if x!=0:
            x-=1

    elif c=='R':
        x+=1

print('('+str(x)+','+str(y)+')')
