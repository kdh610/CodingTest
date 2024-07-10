import math

n = int(input())

stars = []
for _ in range(n):
    x,y = map(float,input().split())
    stars.append((x,y))


distance = []


for i in range(n):
    for j in range(i+1,n):
        dist = round(math.sqrt((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2), 2)
        distance.append((dist, i, j))


parent = [ i for i in range(n) ]

def find(x, parent):

    if not parent[x]==x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(a, b):
    a = find(a,parent)
    b = find(b,parent)

    if a==b: return False

    parent[a] = b
    return True

distance.sort(key=lambda x: x[0])
cnt = 0
cost = 0
for c,a,b in distance:
    if not union(a,b): continue
    cost+=c
    cnt+=1

    if cnt==n:
        break
print(cost)