
from collections import *

n = int(input())
m = int(input())

route = [ [int(1e9)]*(n+1) for _ in range(n+1) ]

graph = [[int(1e9)]*(n+1) for _ in range(n+1)]

for i in range(n+1):
    for j in range(n+1):
        if i==j:
            graph[i][j]=0


for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = min(graph[a][b],c)
    route[a][b] = a



for k in range(1,n+1):
    #print('k',k)
    for a in range(1,n+1):
        for b in range(1,n+1):
            if graph[a][b] > graph[a][k] + graph[k][b]:
                #print(a,k,b)
                graph[a][b] = graph[a][k] + graph[k][b]
                route[a][b]=route[k][b]

for i in range(n+1):
    for j in range(n+1):
        if graph[i][j]==int(1e9):
            graph[i][j]=0


for i in range(1,n+1):
    print(*graph[i][1:])

for i in range(1,n+1):
    for j in range(1,n+1):
        if route[i][j]==int(1e9):
            print(0)
            continue

        cur = j
        result = deque()
        result.append(j)
        while True:
            if route[i][cur] == i:
                result.appendleft(i)
                break

            result.appendleft(route[i][cur])
            cur = route[i][cur]

        print(len(result), *result)