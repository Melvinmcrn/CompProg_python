s=float(input())
if s<0:
    print("ERROR")

else:

    import math
    money=0
    s=math.ceil(s)
    if s>80:
        money+=35+5.5*9+6.5*10+7.5*20+8*20+9*20+(s-80)*10.5

    elif 60<s<=80:
        money+=35+5.5*9+6.5*10+7.5*20+8*20+9*(s-60)

    elif 40<s<=60:
        money+=35+5.5*9+6.5*10+7.5*20+8*(s-40)

    elif 20<s<=40:
        money+=35+5.5*9+6.5*10+7.5*(s-20)

    elif 10<s<=20:
        money+=35+5.5*9+6.5*(s-10)

    elif 1<s<=10:
        money+=35+5.5*(s-1)

    else:
        money=35.0

    print(money)
