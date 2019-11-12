s=input().strip().split()

i=0
total=0
while True:

    if s[i]=='-1':
        break
    total+=int(s[i])
    i+=1

print(total/i)
