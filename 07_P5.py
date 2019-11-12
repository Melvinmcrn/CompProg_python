n=int(input())

num=[]
for i in range(n):

    x=int(input())
    num.append(x)

num.sort(reverse=True)

for c in num:
    print(c)
