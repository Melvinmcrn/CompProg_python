s=input().strip().split()
size=len(s)

if int(s[-2])-int(s[-3])==int(s[-1])-int(s[-2]):

    d=int(s[1])-int(s[0])

    print(int(s[-1])+d)

else:


    d=int(s[-2])-int(s[-4])

    print(int(s[-2])+d)
