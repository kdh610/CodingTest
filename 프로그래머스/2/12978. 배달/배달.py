from collections import *
from heapq import *
def solution(N, road, K):
    graph = defaultdict(list)


    for r in road:
        graph[r[0]].append((r[1],r[2]))
        graph[r[1]].append((r[0], r[2]))

    distance = [int(1e9)]*(N+1)


    def dijkstra(start):

        q = []
        q.append((0,start))
        distance[start]=0
        heapify(q)

        while q:

            dist, cur = heappop(q)

            if dist < distance[cur]:
                continue


            for node, c in graph[cur]:
                cost = dist + c

                if cost < distance[node]:
                    distance[node] = cost
                    heappush(q,(cost,node))


    dijkstra(1)

    answer = 0

    for i in distance:
        if i <=K:
            answer+=1

    return answer