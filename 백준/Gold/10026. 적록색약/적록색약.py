import sys
from collections import *

n=int(input())


picture=[list(sys.stdin.readline().strip()) for _ in range(n)]


dy=[0,0,1,-1]
dx=[1,-1,0,0]
Q=deque()

visit=[[False]*n for _ in range(n)]
normal = defaultdict(int)


for i in range(n):
    for j in range(n):

        if visit[i][j]:
            continue

        cur = picture[i][j]
        normal[cur]+=1

        Q.append((i,j))
        visit[i][j]=True

        if cur=='G':
            picture[i][j]='R'

        while Q:
            y,x=Q.popleft()

            for k in range(4):
                ny=y+dy[k]
                nx=x+dx[k]

                if 0<=ny<n and 0<=nx<n:
                    if picture[ny][nx]==cur and not visit[ny][nx]:
                        Q.append((ny,nx))
                        visit[ny][nx]=True
                        if cur=='G' and picture[ny][nx]=='G':
                            picture[ny][nx]='R'

blind = defaultdict(int)
visit=[[False]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visit[i][j]:
            continue

        cur = picture[i][j]
        blind[cur]+=1

        Q.append((i,j))
        visit[i][j]=True

        while Q:
            y,x=Q.popleft()

            for k in range(4):
                ny=y+dy[k]
                nx=x+dx[k]

                if 0<=ny<n and 0<=nx<n:
                    if picture[ny][nx]==cur and not visit[ny][nx]:
                        Q.append((ny,nx))
                        visit[ny][nx]=True





print(sum(normal.values()), sum(blind.values()))

