import sys

N = int(input())
M = int(input())

link = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]

link.sort(key=lambda x:x[2])



parent = [0] * (N+1)

for i in range(1,N+1):
    parent[i] = i

def find(parent,x):
    if parent[x]!=x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(a,b):
    a = find(parent,a)
    b = find(parent,b)

    if a==b: return False

    parent[b] = a
    return True
sum=0
cnt=0
for i in link:
    a,b,cost = i
    if not union(a,b): continue

    sum += cost
    cnt+=1
    if cnt==N:
        break

print(sum)