n=int(input().strip())

data=dict()
ID_list=[]
for i in range(n):

    x=input().strip()
    
    ID,location=x.split(':')
    ID_list.append(ID.strip())
        
    data[ID.strip()]=set([c.strip() for c in location.strip().split(',')])

order_name=input().strip()
order_location=data[order_name]

out=set()
for ID,location in data.items():
    for c in location:
        
        if ID==order_name:
            break
        
        if c in order_location:
            out.add(ID)

if len(out)>0:
    for c in ID_list:
        if c in out:
            print(c)
else:
    print('Not Found')
