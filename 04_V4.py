x=input().strip()
count=0
for i in x:
    if i>"9" or i<"0":
        print(i,end="")
    else:
        if i=="0":
            print("zero",end="")
        elif i=="1":
            print("one",end="")
        elif i=="2":
            print("two",end="")
        elif i=="3":
            print("three",end="")
        elif i=="4":
            print("four",end="")
        elif i=="5":
            print("five",end="")
        elif i=="6":
            print("six",end="")
        elif i=="7":
            print("seven",end="")
        elif i=="8":
            print("eight",end="")
        elif i=="9":
            print("nine",end="")

        if (count+1)<len(x):
            if "0"<=x[count+1]:
                print(" ",end="")
    count+=1
