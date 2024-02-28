from collections import *
import heapq

N,D = map(int,input().split())


graph = defaultdict(set)
distance = defaultdict(int)
node = set()

for _ in range(N):
    a,b,c = map(int,input().split())
    node.add(a)
    node.add(b)
    graph[a].add((b,c))
    if a!=0:
        graph[0].add((a,a))
    if b<D:
        graph[b].add((D,D-b))
    distance[a] = int(1e9)
    distance[b] = int(1e9)
distance[D] = int(1e9)
graph[0].add((D,D))



for start in node:
    for end in node:
        if start<end:
            graph[start].add((end, end-start))


def dijstra(start):

    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))

    while q:
        dist, node = heapq.heappop(q)

        if dist>distance[node]: continue

        for next in graph[node]:
            cost = dist + next[1]

            if cost<distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q,(cost,next[0]))


dijstra(0)



print(distance[D])