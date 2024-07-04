
import sys

n,m = map(int, sys.stdin.readline().split())
graph = [[int(1e9)]*(n+1) for _ in range(n+1)]

for i in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        graph[i+1][j+1]=arr[j]


for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            if graph[a][b] > graph[a][k] + graph[k][b]:
                graph[a][b] =graph[a][k] + graph[k][b]


for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    if graph[a][b] <= c:
        print("Enjoy other party")
    else:
        print("Stay here")





