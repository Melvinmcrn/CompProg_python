import string

filename = input().strip()
file = open(filename, "r")
word = file.read()
file.close()

word = word.split()
count = dict()

for w in word :
    
    w = w.strip(string.punctuation + string.whitespace)
    w = w.lower()
    count[w] = count.get(w, 0) + 1
    
inverseDict = [(count[c], c) for c in count]
inverseDict.sort(reverse=True)

for i in range(len(inverseDict)-1):
    for j in range(len(inverseDict)-1):

        if inverseDict[j][0] == inverseDict[j+1][0] and inverseDict[j][1]>inverseDict[j+1][1]:
            inverseDict[j],inverseDict[j+1]=inverseDict[j+1],inverseDict[j]

out=[ (c[1],c[0]) for c in inverseDict[:10]]
print(out)
