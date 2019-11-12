w=input().strip()
s=input().strip()

if w in s:
    print('SUBSTRING')

else:

    check=True
    n=-1
    
    for c in w:

        n=s.find(c,n+1)
        if n==-1:
            check=False
            break

    if check:
        print('SUBSEQUENCE')

    else:
        print('NONE')
