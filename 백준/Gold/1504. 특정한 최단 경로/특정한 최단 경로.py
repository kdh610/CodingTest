
import sys
from heapq import *

INF=int(1e9)

n,e = map(int,input().split())

graph=[[] for _ in range(n+1)]

for i in range(e):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a, c))
v1,v2=map(int,input().split())

def dijkstra(start):
    distance = [INF] * (n + 1)
    q=[]
    heappush(q,(0,start))
    distance[start]=0

    while q:
        dist, now=heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]]=cost
                heappush(q,(cost,i[0]))
    return distance


if dijkstra(1)[v1]==INF or dijkstra(v1)[v2]==INF or dijkstra(v2)[n]==INF:
    print(-1)
else:
    print(min(dijkstra(1)[v1] + dijkstra(v1)[v2] + dijkstra(v2)[n], dijkstra(1)[v2] + dijkstra(v2)[v1] + dijkstra(v1)[n]))
    

