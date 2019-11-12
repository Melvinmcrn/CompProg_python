import math

bd, bm, by, d, m, y = [int(e) for e in input().split()]
y-=543
by-=543
day=0

#year in the middle
day+=(y-by-1)*365
#print('y',day)

#day2
day+=d
#print('d',day)

#month2
m-=1
while m>0:
    if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
        day+=31

    elif m==4 or m==6 or m==9 or m==11:
        day+=30
        
    elif m==2:
        n=28

        if y%400==0:
            n=29

        if y%4==0 and y%100!=0:
            n=29

        day+=n

    m-=1
#    print('m',day)

#month1 and day1
bmonth=bm
bmonthday=0
bm+=1
while bm<13:
    if bm==1 or bm==3 or bm==5 or bm==7 or bm==8 or bm==10 or bm==12:
        day+=31

    elif bm==4 or bm==6 or bm==9 or bm==11:
        day+=30
        
    elif bm==2:
        n=28

        if by%400==0:
            n=29

        if by%4==0 and by%100!=0:
            n=29

        day+=n
        
    if bmonth==1 or bmonth==3 or bmonth==5 or bmonth==7 or bmonth==8 or bmonth==10 or bmonth==12:
        bmonthday=31
#        print('31 yeah')
            
    elif bmonth==4 or bmonth==6 or bmonth==9 or bmonth==11:
        bmonthday=30
#        print('30 yeah')
        
    elif bmonth==2:
        n=28

        if by%400==0:
            n=29

        if by%4==0 and by%100!=0:
            n=29

        bmonthday=n

    bm+=1
#    print('bm',day)
#    print('bmd',bmonthday)
#    print('bmonth',bmonth)

#day1
if bmonthday!=0:
    day+=(bmonthday-bd)
#print('bd',day)

physical="{:.2f}".format(math.sin(2*math.pi*day/23))
emotional="{:.2f}".format(math.sin(2*math.pi*day/28))
intellectual="{:.2f}".format(math.sin(2*math.pi*day/33))

print(day,physical,emotional,intellectual)
