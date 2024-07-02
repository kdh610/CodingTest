import sys

n,m = map(int, input().split())

height = list(map(int, sys.stdin.readline().split()))

jokyo = []

for _ in range(m):
    a,b,k = map(int, sys.stdin.readline().split())
    jokyo.append((a,b,k))

prefix = [0] * (n+1)

for a,b,k in jokyo:
    prefix[a-1]+=k
    prefix[b]+=(k*-1)


for i in range(1,len(prefix)):
    prefix[i]+=prefix[i-1]

for i in range(n):
    height[i] += prefix[i]


print(*height[:n])
