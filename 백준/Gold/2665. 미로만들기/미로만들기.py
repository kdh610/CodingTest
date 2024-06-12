

from collections import *

n = int(input())

maze = [ list(input()) for _ in range(n) ]
temp = [ [0]*n for _ in range(n)]
visit = [ [False]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if maze[i][j] == '1':
            maze[i][j] = 0
        elif maze[i][j]=='0':
            maze[i][j] = '#'



dy = [0,0,1,-1]
dx = [1,-1,0,0]

q = deque()

q.append((0,0))

while q:
    y, x = q.popleft()

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0<=ny<n and 0<=nx<n:
            if maze[ny][nx] == '#':
                if not visit[ny][nx]:
                    temp[ny][nx] = temp[y][x] +1
                    visit[ny][nx] = True
                    q.append((ny, nx))
                else:
                    temp[ny][nx] = min(temp[ny][nx], temp[y][x]+1)

            else:
                if not visit[ny][nx]:
                    temp[ny][nx] = temp[y][x]
                    visit[ny][nx] =True
                    q.appendleft((ny,nx))
                else:
                    temp[ny][nx] = min(temp[ny][nx], temp[y][x])


print(temp[n-1][n-1])

