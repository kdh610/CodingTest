from collections import *
from heapq import *
def solution(n, roads, sources, destination):
    graph = defaultdict(list)
    for i in roads:
        a,b=i[0],i[1]
        graph[a].append((b,1))
        graph[b].append((a,1))


    def dijkstra(start):
        distance = [int(1e9)] * (n + 1)
        Q = deque()
        Q.append((0,start))
        distance[start]= 0

        while Q:
            dist, now = Q.popleft()

            if distance[now]<dist:
                continue

            for i in graph[now]:
                cost = dist + i[1]
                if cost<distance[i[0]]:
                    distance[i[0]]=cost
                    Q.append((cost, i[0]))
        return distance
    
    answer=[]
    distance = dijkstra(destination)

    for source in sources:
        if distance[source]==int(1e9):
            answer.append(-1)
        else:
            answer.append(distance[source])
    return answer