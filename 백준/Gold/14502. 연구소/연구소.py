import sys
from collections import *

n,m = map(int,sys.stdin.readline().split())
maps=[]
space = []
virus = []
no_zero = 0
for i in range(n):
    maps.append(list(map(int,sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        if maps[i][j]==0:
            space.append((i,j))
        else:
            if maps[i][j]==2:
                virus.append((i,j))
            no_zero += 1
N=len(space)
area = n*m
safe = area - no_zero - 3

def bfs(y,x):
    Q = deque()
    Q.append((y,x))
    cnt = 0
    visit[y][x]=True
    while Q:
        y,x = Q.popleft()
        for dy,dx in [(0,1),(0,-1),(1,0),(-1,0)]:
            ny = y + dy
            nx = x + dx
            if 0<=ny<n and 0<=nx<m:
                if maps[ny][nx] == 2:
                    if visit[ny][nx] == False:
                        visit[ny][nx] = True
                        Q.append((ny, nx))
                if maps[ny][nx]==0:
                    if visit[ny][nx] == False:
                        visit[ny][nx] = True
                        cnt += 1
                        Q.append((ny,nx))
    return cnt

y1,x1 = space[0]
y2,x2 = space[1]
y3,x3 = space[2]
answer = 0

for i,w1 in enumerate(space):
    if maps[y1][x1] == 1:
        maps[y1][x1]=0
    y1,x1 = w1
    maps[y1][x1] = 1
    for j,w2 in enumerate(space[i+1:],start=i+1):
        if maps[y2][x2] == 1:
            maps[y2][x2] = 0
        y2,x2 = w2
        maps[y2][x2] = 1
        for k,w3 in enumerate(space[j+1:]):
            if maps[y3][x3] == 1:
                maps[y3][x3] = 0
            y3,x3 = w3
            maps[y3][x3]=1
            visit = [[False] * m for _ in range(n)]
            max_vi = 0
            # print(maps)
            for y,x in virus:
                # print(y,x)
                max_vi += bfs(y,x)
            result = safe - max_vi
            answer = max(answer,result)
            # print('maxvi', max_vi)
            # print('result', result)
            # print('answer',answer)

print(answer)
