mode=input().strip()
s=input().strip()
findwhat=input().strip()
replace=input().strip()

if mode=="R":
    
    start=s.lower().find(findwhat.lower())
    stop=start+len(findwhat.lower())
    #print("start=",start,"stop=",stop)
    s=s[:start]+replace+s[stop:]

elif mode=="RA":

    start=0
    while s.lower().find(findwhat.lower(),start)!=-1:

        where=s.lower().find(findwhat.lower(),start)
        s=s[:where]+replace+s[where+len(findwhat):]
        start=where+len(replace)

print(s)
