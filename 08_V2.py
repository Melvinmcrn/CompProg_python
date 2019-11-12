file=open('file1.txt')

data1=set()
for line in file:

    line=line.strip()
    for i in range(len(line)):

        if line[i] in ''''"-.(),''':
            line=line[:i]+' '+line[i+1:]

    line=line.lower()
    data1.update(line.split())

file.close()

file=open('file2.txt')

data2=set()
for line in file:

    line=line.strip()
    for i in range(len(line)):

        if line[i] in ''''"-.(),''':
            line=line[:i]+' '+line[i+1:]

    line=line.lower()
    data2.update(line.split())

file.close()

word=input().strip()

if word in data1 and word in data2:
    print('Found in both files')

elif word in data1:
    print('Found in file1 only')

elif word in data2:
    print('Found in file2 only')

else:
    print('Not found')
