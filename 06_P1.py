s=[]

while True:

    x=int(input())
    s.append(x)

    if x<0:
        break

for i in range(len(s)-1):

    print(s[i]+s[-1])

