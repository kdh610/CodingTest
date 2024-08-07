
from itertools import *

n,m = map(int, input().split())

road = [ [int(1e9)] *(n+1) for _ in range(n+1) ]


for _ in range(m):
    a,b = map(int,input().split())

    road[a][b]= 1
    road[b][a] = 1

for i in range(n+1):
    for j in range(n+1):
        if i==j:
            road[i][j]= 0


for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            road[a][b] = min(road[a][b], road[a][k]+road[k][b])


#print(*road, sep='\n')

buildings = [ i for i in range(1,n+1)]


#print(list(combinations(buildings,2)))

time = int(1e9)
answer = []
for c in combinations(buildings,2):
    a, b = c
    #print('a,b',a,b)
    temp = 0
    for i in range(1,n+1):

        temp += min(road[i][a], road[i][b])
    #print(temp)
    if temp < time:
        time = temp
        answer = [a, b, temp*2]

print(*answer)