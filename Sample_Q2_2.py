n=int(input())
start,stop,step=[int(x) for x in input().split()]

if n!=10:
    num=0
    for i in range(len(str(start))-1,-1,-1):
        num+=(int(str(start)[i]))*n**(len(str(start))-i-1)

    start=num
    num=0
    for i in range(len(str(stop))-1,-1,-1):
        num+=int(str(stop)[i])*n**(len(str(stop))-i-1)

    stop=num
    num=0
    for i in range(len(str(step))-1,-1,-1):
        num+=int(str(step)[i])*n**(len(str(step))-i-1)

    step=num
    for i in range(start,stop,step):
        num=i
        out=""
        if start==0 and i==start:
            out='0'
        while num>0:
            out=str((num%n))+out
            num//=n

        print(out)

else:
    for i in range(start,stop,step):
        print(i)
