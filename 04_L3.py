x_main=input().strip()
y_main=input().strip()
size=len(y_main)
x,y=x_main.lower(),y_main.lower()
check="YES"

for i in range(size):
    
    if y[i] in x:
        x=x[:x.find(y[i])]+x[x.find(y[i])+1:]
        
    elif y[i]!=" ":
        
        check="NO"
        break

x=x.strip()

if len(x)!=0:
    check="NO"

if check=="YES":
    print(x_main)
elif check=="NO":
    print(x_main,y_main)
