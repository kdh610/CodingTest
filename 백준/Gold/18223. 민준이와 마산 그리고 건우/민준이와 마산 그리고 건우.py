import sys
import heapq

input = sys.stdin.readline

V,E,P = map(int,input().split())

INF = int(1e9)
graph = [[] for _ in range(V+1)]


for _ in range(E):
    a,b,c = map(int,input().split())

    graph[a].append((b,c))
    graph[b].append((a,c))




def dijstra(start):
    distance = [INF] * (V + 1)
    distance[start] =0

    q = []

    heapq.heappush(q,(0,start))

    while q:

        dist, node = heapq.heappop(q)

        if dist>distance[node]:
            continue

        for i in graph[node]:
            cost = dist + i[1]
            if cost<=distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

    return distance


a = dijstra(1)
b = dijstra(P)

if(a[V]>= a[P]+b[V]):
    print("SAVE HIM")
else:
    print("GOOD BYE")