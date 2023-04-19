

n = int(input())
m = int(input())

graph = [list(map(int,input().split())) for _ in range(n)]
plan = list(map(int,input().split()))

parent = [ i for i in range(n)]

def find(parent,x):
    if parent[x] !=x:
        parent[x] = find(parent, parent[x])

    return parent[x]

def union(parent, a,b):
    a=find(parent,a)
    b = find(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(n):
    for j in range(n):
        if graph[i][j]==1 and find(parent,i)!=find(parent,j):
            union(parent,i,j)

answer = 'YES'
root = parent[plan[0]-1]
for p in plan:
    if parent[p-1] != root:
        answer="NO"
        break

print(answer)