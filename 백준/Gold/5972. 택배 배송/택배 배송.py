import sys
from heapq import *

n ,m = map(int,input().split())

graph = [[] for _ in range(n+1)]
INF = int(1e9)

for i in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

distance=[INF]*(n+1)


def dijkstra(start):
    q = []
    distance[start] = 0

    heappush(q,(0,start))

    while q:
        dis, node =heappop(q)
        if distance[node] <dis:
            continue

        for i in graph[node]:
            cost = dis + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heappush(q,(cost,i[0]))


dijkstra(1)

print(distance[n])