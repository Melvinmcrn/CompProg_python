x=[int(e) for e in input().split()]
m=input().strip()

if m=='a':

    for i in range(len(x)-1):
        for j in range(len(x)-1):

            if int(x[j])>int(x[j+1]):

                x[j],x[j+1]=x[j+1],x[j]

else:
    
    for i in range(len(x)-1):
        for j in range(len(x)-1):

            if int(x[j])<int(x[j+1]):

                x[j],x[j+1]=x[j+1],x[j]

print(x)
