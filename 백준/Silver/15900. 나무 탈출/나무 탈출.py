from collections import *
import sys
n = int(input())


tree = defaultdict(list)

for _ in range(n-1):
    a, b = map(int,sys.stdin.readline().split())

    tree[a].append(b)
    tree[b].append(a)


visit = [False]*(n+1)

Q= deque()
visit[1] = True
Q.append((1,0))
depth = 0
total=0

while Q:
    start, depth = Q.popleft()
    for i in tree[start]:
        if visit[i] and len(tree[start])==1:
            total+=depth
        if visit[i]:
            continue

        visit[i] = True
        Q.append((i,depth+1))


# print(total)
if total%2==0:
    print("No")
else:
    print("Yes")






# total = 0
# count = 1
# def dfs(start, depth):
#     global total
#     global count
#     for i in tree[start]:
#         if start==1:
#             length = 0
#         print('======start', start)
#         print('i, depth',i,depth)
#         if visit[i]:
#             print('방문')
#             continue
#         visit[i] = True
#
#         dfs(i,depth+1)
#         depth=0
#
#
#     print('start, leaft',start, depth)
#     total+=depth
#
#
# dfs(1,1)
#
# print(total)
