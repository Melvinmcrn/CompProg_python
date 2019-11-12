n=int(input())

winnerdata=set()
loserdata=set()
for i in range(n):

    winner,loser=input().strip().split()

    if winner not in loserdata:
        winnerdata.add(winner)
        
    winnerdata.discard(loser)
    loserdata.add(loser)

print(sorted(list(winnerdata)))
