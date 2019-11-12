file=open("data.txt", "r")

n=int(input())
i=0
found=False

for line in file:

    if 'Name' in line:
        i+=1

    if i==n:
        print(line[line.find('Name: ')+6:len(line)-1])
        found=True
        break

if not found:
    print('Not Found')

file.close()
