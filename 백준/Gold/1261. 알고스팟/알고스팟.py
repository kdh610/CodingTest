
from collections import *
import copy
m,n = map(int,input().split())

maze = [list(input()) for _ in range(n)]

visit = [ [False]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        maze[i][j] = int(maze[i][j])
        if maze[i][j] == 1:
            maze[i][j]= '#'

temp = copy.deepcopy(maze)
dy = [0,0,1,-1]
dx = [1,-1,0,0]

Q = deque()
Q.append((0,0))
visit[0][0] = True


while Q:
    y,x = Q.popleft()

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0<=ny<n and 0<=nx<m:

            if not visit[ny][nx]:
                if maze[ny][nx]=='#':
                    temp[ny][nx]=int(temp[y][x]) +1
                    Q.append((ny,nx))
                else:
                    temp[ny][nx] = int(temp[y][x])
                    Q.appendleft((ny, nx))
                visit[ny][nx] = True
            else:
                if maze[ny][nx]==0:
                    temp[ny][nx] = min(temp[ny][nx], temp[y][x])
                else:
                     temp[ny][nx] = min(temp[ny][nx], temp[y][x]+1)


print(temp[n-1][m-1])
