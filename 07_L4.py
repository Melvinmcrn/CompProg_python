file=open('inventory.txt')

inventory=[]
for line in  file:

    line=line.strip()
    code,name,amount=line.split(';')
    inventory.append([code,name,int(amount)])

file.close()

while True:

#    print(inventory)
    order=input().strip().split()

    if order[0]=='T':

        for c in inventory:

            if order[1] in c:

                position=inventory.index(c)
                inventory[position][2]+=int(order[2])
                print(inventory[position])
                break

        else:
            print('Product code does not exist.')

    elif order[0]=='U':

        for c in inventory:

            if order[1] in c:

                position=inventory.index(c)
                inventory[position][2]=int(order[2])
                print(inventory[position])
                break

        else:
            print('Product code does not exist.')

    elif order[0]=='A':

        for c in inventory:

            if order[1] in c:

                print('Duplicate product code.')
                break

        else:
            order[3]=int(order[3])
            inventory.append(order[1:])
            print(order[1:])

    elif order[0]=='D':

        for c in inventory:

            if order[1] in c:

                position=inventory.index(c)
                inventory.pop(position)
                print(order[1],'deleted')
                break

        else:
            print('Product code does not exist.')
    
    elif order[0]=='Q':

        print('Bye!')
        break
