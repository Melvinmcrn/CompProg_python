data=input().strip().split()

for i in range(len(data)):
    data[i]=int(data[i])

player1=0
player2=0

while True:

    position=data.index(max(data[0],data[-1]))
    player1+=int(data.pop(position))

    if len(data)==0:
        break

    position=data.index(max(data[0],data[-1]))
    player2+=int(data.pop(position))

    if len(data)==0:
        break

print(player1)
print(player2)

if player1>player2:
    print('1')

elif player2>player1:
    print('2')

else:
    print('0')
