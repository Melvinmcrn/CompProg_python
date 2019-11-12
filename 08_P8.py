list1=tuple(e for e in input().strip().split())
list2=tuple(e for e in input().strip().split())
word=tuple(e for e in input().strip().split())

out=''

for c in word:

    if c in list1:
        out+=list2[list1.index(c)]+' '

    elif c in list2:
        out+=list1[list2.index(c)]+' '

    else:
        out+=c+' '

print(out.strip())
