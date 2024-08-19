import sys

N, Q = map(int, input().split())

logs = [(-1,-1,0)]
jump = []
for i in range(N):
    x1, x2, y = map(int, sys.stdin.readline().split())
    logs.append((x1,x2,i+1))

for _ in range(Q):
    a,b = map(int,sys.stdin.readline().split())
    jump.append((a,b))

logs.sort(key=lambda x: (x[0]))

parent = [ i for i in range(N+1)]

def find(parent, x):
    if parent[x]!=x:
        parent[x] = find(parent, parent[x])

    return parent[x]

def union(a,b,parent):
    a = find(parent,a)
    b = find(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a]=b

    return True




minX = logs[1][0]
maxX = logs[1][1]


for i in range(2,N+1):
    x1, x2, num = logs[i]

    if x1 <= maxX:
        union(logs[i-1][2], num, parent)
        maxX = max(maxX, x2)
        minX = min(minX, x1)

    else:
        maxX=x2
        minX = x1



for i in range(Q):
    a, b = jump[i]

    if find(parent,a)==find(parent,b):
        print(1)
    else:
        print(0)


