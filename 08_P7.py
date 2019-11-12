n=int(input())

data=dict()
word_data=tuple()
for i in range(n):

    x,word=input().strip().split('\t')
    word_data+=tuple([word])

    if word[:2] not in data:
        data[word[:2]] = 1

    else:
        data[word[:2]]+=1

most=0
out=[]
for c,n in data.items():

    if n>most:
        most=n
        out=[c]
        
    elif n==most:
        out.append(c)

out.sort()
ans=out[0]
print(ans)
print(data[ans])
for c in word_data:

    if c[:2]==ans:
        print(c)
