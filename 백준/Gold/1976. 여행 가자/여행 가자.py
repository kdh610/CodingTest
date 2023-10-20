import sys

N = int(input())
M = int(input())

cities = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
plan = list(map(int,sys.stdin.readline().split()))

parent = [i for i in range(N+1)]

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])

    return parent[x]

def union(parent, a,b):
    a = find(parent,a)
    b = find(parent,b)

    if a>b:
        parent[a]=b
    else:
        parent[b]=a


for i in range(N):
    for j in range(N):
        if cities[i][j]==1:
            union(parent,i+1,j+1)





answer = "YES"
start = plan[0]

for i in plan:
    end = i
    if find(parent,start) != find(parent,end):
        answer="NO"
        break
    start = i

print(answer)