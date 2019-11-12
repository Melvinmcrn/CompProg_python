def add_person(data,x,i):

    for c in x[1:]:
        if c not in data[i][1]:
            data[i][1].append(c)

    return data

#----------------------------------------------------------
def sort_data(data,mask_list):
    for i in range(len(data)):
        for j in range(len(data)-1):

            if len(data[j][1]) > len(data[j+1][1]):
                data[j], data[j+1] = data[j+1], data[j]

            elif len(data[j][1]) == len(data[j+1][1]) and mask_list.index(data[j][0]) > mask_list.index(data[j+1][0]):
                data[j], data[j+1] = data[j+1], data[j]
                              
    return data

#-----------------------------------------------------------
data = []
mask_list = []

while True:

    x = input().strip().split()
    if x == ['end']:
        break

    if x[0] not in mask_list:
        mask_list.append(x[0])
        
    for i in range(len(data)):
        if x[0] == data[i][0]:
            data = add_person(data,x,i)
            break
    else:
        data.append([x[0],[]])
        data = add_person(data,x,-1)

#---------------------------------------------------------------
out = []
person = set()
n = len(data)

while len(data) > 0:

    data = sort_data(data,mask_list)

    for c in data[0][1]:
        if c not in person:
            out.append([data[0][0],c])
            person.add(c)
            break

    data.pop(0)

    for i in range(len(data)):
        if out[-1][1] in data[i][1]:
            data[i][1].pop(data[i][1].index(out[-1][1]))

for c in out:
    print(c[0],c[1])
