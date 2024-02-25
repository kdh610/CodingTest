import sys

N,M = map(int,input().split())

edge = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]


edge.sort(key=lambda x:x[2])

parent = [0]*(N+1)

for i in range(N+1):
    parent[i] = i

def find(parent,x):
    if not parent[x]==x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(a,b):
    a=find(parent,a)
    b=find(parent,b)

    if a==b: return False
    parent[b]=a
    return True

cost = 0
cnt = 0
split_cost = 0
for i in edge:
    a,b,c = i

    if not union(a,b): continue
    cost+=c
    cnt+=1
    split_cost=max(split_cost,c)
    if cnt==N-1:
        break

print(cost-split_cost)

