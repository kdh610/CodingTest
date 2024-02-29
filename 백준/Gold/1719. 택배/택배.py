import sys
import heapq

input = sys.stdin.readline

n,m = map(int,input().split())


graph = [[] for _ in range(n+1)]


for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))






def dijstra(start):
    result = ['-'] * (n+1)
    distance = [int(1e9)] * (n + 1)
    q=[]
    distance[start]=0
    heapq.heappush(q,(0,start))

    while q:
        dist, cur = heapq.heappop(q)

        if dist>distance[cur]: continue

        for node in graph[cur]:
            cost = dist + node[1]
            if cost<distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q,(cost,node[0]))

                result[node[0]] = result[cur]
                if cur==start:
                    result[node[0]] = node[0]



    print(*result[1:])


for i in range(1,n+1):
    dijstra(i)