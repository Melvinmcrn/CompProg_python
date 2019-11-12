num,r=[int(x) for x in input().split()]
n=(num%10**r)//10**(r-1)

if n<5:
    num=(num//10**(r))*10**r
    #print('case1')

elif n>5:
    num=(num//10**(r))*10**r
    num+=10**(r)
    #print('case2')

elif n==5:
    num=(num//10**(r))*10**r
    if ((num//10**r)%10)%2!=0:
        num+=10**r
    #print('case3')

print(num)
