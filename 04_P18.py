n=int(input())

word=""
size=[]

for i in range(n):
    x=input().strip().lower()
    size.insert(i,len(x))
    word+=x

#Prefix
prefix=""
for i in range(int(size[0])):
    
    letter=word[i]
    check=0
    sizemove=0
    for j in range(1,n):
        
        sizemove+=size[j-1]
        if letter != word[i + sizemove ]:
            check=-1
            break

    if check==-1:
        break
    else:
        prefix+=word[i]

if prefix in "":
    print("NO COMMON PREFIX")
else:
    print(prefix)

#Suffix
suffix=""
for i in range(int(size[0])):
    
    letter=word[len(word)-i-1]
    check=0
    sizemove=0
    for j in range(1,n):

        sizemove+=size[n-j]
        if letter!=word[len(word)-(1+i+sizemove)]:
            check=-1
            break

    if check==-1:
        break
    else:
        suffix=word[len(word)-(1+i+sizemove)]+suffix

if suffix in "":
    print("NO COMMON SUFFIX")
else:
    print(suffix)
