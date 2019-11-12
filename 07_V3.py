file=open('hotels.txt')
hotels=[]

for line in file:
    [hotel, stars, review] = line.split(';')
    hotels.append([hotel, int(stars), float(review)])

file.close()

#print(hotels)

star=int(input())
found_hotels=[]
hotels_review=[]

check=True
for h in hotels:
    if h[1]>=star:

        found_hotels.append(h)
        hotels_review.append(h[2])

if len(found_hotels)==0:
    print('Not Found')

while len(hotels_review)>0:

    i=hotels_review.index(max(hotels_review))
    print(found_hotels[i][0],found_hotels[i][1],found_hotels[i][2])
    found_hotels.pop(i)
    hotels_review.pop(i)
