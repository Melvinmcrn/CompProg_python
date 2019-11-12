s=input().strip()
longest=0
current_length=0
last_char=""
s=s.lower()
x=s[0]
for i in s:
   
    if i!=last_char:
                    
        if current_length>longest:
            longest=current_length
            
        current_length=1
        last_char=i

    else:
        current_length+=1

if current_length>longest:
    longest=current_length

print(longest)
                
