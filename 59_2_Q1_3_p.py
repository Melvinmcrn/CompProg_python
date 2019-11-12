a,b,c = [float(x) for x in input().split()]
t = b*b - 4*a*c

if t<0:
    print("Roots are complex numbers")

elif a==0 and b==0 and c==0:
    print("Roots are any numbers")

elif a==0 and b==0:
    print("No roots exists")

elif a==0:

    print("{:.2f}".format(-c/b))

else:
    r1 = (-b+t**0.5)/(2*a)
    outr1 = "{:.2f}".format(r1)
    r2 = (-b-t**0.5)/(2*a)
    outr2 = "{:.2f}".format(r2)
    #print('r1=',r1)
    #print('r2=',r2)
    #if r1<r2:
     #   print('yes')

    if r1==r2:
        print(outr1)

    else:
        if r1<r2:
            print(outr1,outr2)

        elif r2<r1:
            print(outr2,outr1)
