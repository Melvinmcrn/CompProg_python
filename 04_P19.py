s1=input().strip()
s2=input().strip()
check=False
alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
out=""

for c in alphabet:

    if c in s1 and c in s2:
        if check:
            out+=" "+c

        else:
            out+=c
            check=True

if check:
    print(out)
else:
    print('NONE')
