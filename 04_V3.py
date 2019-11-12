s=input().strip()
w=input().strip()
s=s.lower()+" "
w=w.lower()
check=""
for i in s:
    
    if i!=" " and i!='"' and i!="'" and i!="," and i!=".":
        check+=i
    if (i==" " or i=='"' or i=="'" or i=="," or i==".") and check==w:
        print("Found")
        break
    elif (i==" " or i=='"' or i=="'" or i=="," or i==".") and check!=w:
        check=""
    
if check!=w:
    print("Not Found")
