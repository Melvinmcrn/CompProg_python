s=input().strip().lower()
check=0

for i in range(len(s)):

    if s[i] in "aeiou" and s[i-1] in "aeiou" and i>0:
        i=i
    elif s[i] in "aeiou":
        check+=1

print(check)
