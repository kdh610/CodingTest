import sys
INF=int(1e9)
n,m = map(int,input().split())

friends = [[INF] *(n+1) for _ in range(n+1)]


for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    friends[a][b] =1
    friends[b][a] = 1

for i in range(n+1):
    for j in range(n+1):
        if i==j:
            friends[i][j]=0

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            friends[a][b] = min(friends[a][b], friends[a][k]+friends[k][b])

kevin = INF

for i in range(1,n+1):
    if kevin > sum(friends[i][1:]):
        kevin=sum(friends[i][1:])
        answer = i

print(answer)