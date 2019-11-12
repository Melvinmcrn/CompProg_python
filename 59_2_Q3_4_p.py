n = int(input())

data=dict()

for i in range(n):
    tel,vote = input().strip().split(',')
    if vote not in data:
        data[vote] = {tel}
    else:
        data[vote] = data[vote] | {tel}

out=[]
for i,v in data.items():
    out.append([len(v),i])

for i in range(len(out)):
    for j in range(len(out)-1):
        if out[j][0]<out[j+1][0]:
            out[j], out[j+1] = out[j+1], out[j]
        elif out[j][0]==out[j+1][0] and out[j][1]>out[j+1][1]:
            out[j], out[j+1] = out[j+1], out[j]
            
print_out=''
for i in range(len(out)):
    print_out+=out[i][1]+','
    if i==2:
        break

print(print_out[:-1])
