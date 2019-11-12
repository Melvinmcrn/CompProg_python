n=int(input())

file=open("cards.txt", "r")

count=1
for line in file:

    if count==n:
        check=True
        line=line[:-1]
        for i in range(1,len(line)):
            a1=line[i-1]
            a2=line[i]
            if a1=='A':
                a1=1
            elif a1=='0':
                a1=10
            elif a1=='J':
                a1=11
            elif a1=='Q':
                a1=12
            elif a1=='K':
                a1=13

            if a2=='A':
                a2=1
            elif a2=='0':
                a2=10
            elif a2=='J':
                a2=11
            elif a2=='Q':
                a2=12
            elif a2=='K':
                a2=13

            if int(a1)>int(a2):
                print('N')
                check=False
                break
            
    count+=1

if check:
    print('Y')
