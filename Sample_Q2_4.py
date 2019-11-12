s=input().strip()

letter='abcdefghijklmnopqrstuvwxyz'
word=''
palin_max=''

for i in range(len(s)):
    for j in range(i,len(s)+1):

        word=s[i:j]

        if word==word[::-1]:
            
            if len(word)>len(palin_max):
                palin_max=word

            elif len(word)==len(palin_max):
                
                check=True
                for k in range(len(word)):

                    if letter.find(word[k])>letter.find(palin_max[k]):
                        check=False
                        break

                if check:
                    palin_max=word

print(palin_max)
