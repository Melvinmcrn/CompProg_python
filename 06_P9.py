data= input().strip().split()
order=input().strip().split()

out=''
for i in order:

    out+=data[int(i)]+' '

print(out.strip())
