temp=tuple(input().strip().split())

data=set()
discard_set=set()
for c in temp:

    if int(c) in data:
        discard_set.add(int(c))

    data.add(int(c))

for c in discard_set:
    data.discard(int(c))

if len(data)>0:
    print(min(data))

else:
    print('NONE')
