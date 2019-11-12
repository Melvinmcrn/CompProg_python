def roman_to_int(string):

    table=[['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90], \
           ['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',4],['I',1]]
    returnint=0

    for pair in table:
        check=True
        while check:
            if len(string)>=len(pair[0]):
                if string[0:len(pair[0])]==pair[0]:
                    returnint+=pair[1]
                    string=string[len(pair[0]):]
                else: check=False
            else: check=False

    return returnint

#main---------------------------------------------------------------------

n=int(input())

data=[]

for i in range(n):
    x=input().strip()
    data.append([x,roman_to_int(x)])

for i in range(len(data)):
    for j in range(len(data)-1):

        if data[j][1]>data[j+1][1]:
            data[j], data[j+1] = data[j+1], data[j]

for c in data:
    print(c[0])

