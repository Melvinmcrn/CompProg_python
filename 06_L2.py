num_list=input().strip().split()

out_list=[]
count=0

for c in num_list:

    if int(c)%2==0:
        out_list.append(0)
    else:
        out_list.append(1)
        count+=1

print(out_list)
print(count)
