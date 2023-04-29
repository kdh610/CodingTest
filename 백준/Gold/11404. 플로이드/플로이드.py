import sys
import heapq
INF = int(1e9)
n = int(input())
m=int(input())
graph=[[INF]*(n+1) for _ in range(n+1)]

for i in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    if c < graph[a][b]:
        graph[a][b] = c

for i in range(n+1):
    for j in range(n+1):
        if i==j:
            graph[i][j] =0


for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k] + graph[k][b])


for a in range (1, n + 1 ):
    for b in range (1, n + 1 ):
# 도달할 수 는 경우, 을 출력
        if graph[a][b ] == INF :
            print(0, end= " ")
# 도달할 수 있는 경우 거 리를 출력
        else:
            print(graph[a ][b], end=" ")
    print()

