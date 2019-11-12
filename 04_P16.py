s=input().strip()
out=""
n=-1
while True:
    
    n=s.find(',',n+1)
    if n==-1:
        break
    else:
        s=s[:n]+s[n+1:]
        n-=1
num,decimal="",""
if s.find('.')!=-1:
    decimal=s[s.find('.'):]
    num=s[:s.find('.')]
else:
    num=s

if s[0]=='-':
    out+='lop-'
    num=num[1:]

for i in range(len(num)):

    if num[i]=='0' and len(num)==1:
        out+='soon-'
    elif num[i]=='1' and len(num)>1 and (i==len(num)-1 or i==len(num)-7):
        out+='ed-'
    elif num[i]=='1' and (i!=len(num)-2 and i!=len(num)-8):
        out+='nueng-'
    elif num[i]=='2' and (len(num)-i-1==1 or len(num)-i-1==7):
        out+='yee-'
    elif num[i]=='2':
        out+='song-'
    elif num[i]=='3':
        out+='sam-'
    elif num[i]=='4':
        out+='see-'
    elif num[i]=='5':
        out+='ha-'
    elif num[i]=='6':
        out+='hok-'
    elif num[i]=='7':
        out+='jed-'
    elif num[i]=='8':
        out+='pad-'
    elif num[i]=='9':
        out+='kao-'
        
    luk=len(num)-i-1
    if num[i]!='0' or luk==6:
        if luk==1 or luk==7:
            out+='sip-'
        elif luk==2 or luk==8:
            out+='roey-'
        elif luk==3 or luk==9:
            out+='pun-'
        elif luk==4:
            out+='muen-'
        elif luk==5:
            out+='saen-'
        if luk==6 or (luk==6 and num[i]=='0'):
            out+='larn-'
#print('out num=',out)

for c in decimal:
    #print('decimal c=',c)
    if c =='.':
        out+='jood-'
    elif c=='1':
        out+='nueng-'
    elif c=='2':
        out+='song-'
    elif c=='3':
        out+='sam-'
    elif c=='4':
        out+='see-'
    elif c=='5':
        out+='ha-'
    elif c=='6':
        out+='hok-'
    elif c=='7':
        out+='jed-'
    elif c=='8':
        out+='pad-'
    elif c=='9':
        out+='kao-'
    elif c=='0':
        out+='soon-'
    #print(out)

print(out[:len(out)-1])
