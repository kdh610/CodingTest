
import sys

v,e = map(int,input().split())

city = [ [int(1e9)]*(v+1) for _ in range(v+1)]

for i in range(e):
    a,b,c = map(int,sys.stdin.readline().split())
    city[a][b]=c


# print(*city,sep='\n')
# print()

for k in range(1,v+1):
    for a in range(1,v+1):
        for b in range(1,v+1):
            city[a][b] = min(city[a][b], city[a][k]+city[k][b])

# print(*city,sep='\n')
answer = int(1e9)
for i in range(1,v+1):
    answer = min(answer, city[i][i])

if answer==int(1e9):
    print(-1)
else:
    print(answer)